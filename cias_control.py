""" cias_control.py

Trying to interact with a Crestron MD8x8 over telnet

Requirements
------------
telnetlib : maybe this would work
cias_globals : Global junk
"""

import telnetlib
import cias_globals


class CiasControl(object):
    def __init__(self):
        self.host = cias_globals.config['cias'].get('CrestronHostname')

        # Assuming a DM-MD8x8, because that's what I have
        # Build an array to reference the card names vs chassis #s
        # Use this with e.g. self.cardsInput[2] to get back ['Input 2 Name', card_2_#]
        # awareness that the array is 0 indexed, so card 1 will be array[0], card 2 is array[1] etc
        # u know
        self.cardsInput = []
        for i in range(1, 9):
            self.cardsInput.append([cias_globals.config['cias'].get('input{}Name'.format(i)),
                                    cias_globals.config['cias'].get('input{}Card'.format(i))])

        self.cardsOutput = []
        for i in range(1, 9):
            self.cardsOutput.append([cias_globals.config['cias'].get('output{}Name'.format(i)),
                                     cias_globals.config['cias'].get('output{}Card'.format(i))])

    def send_command(self, telnet_cmd):
        # Connect to self.host.  The DM-MD8x8 by default has no un/pw
        cias_globals.debugger.message("TELN", "Telnet cnnect: {}".format(self.host))
        telnet = telnetlib.Telnet(self.host)
        # read_until will block until timeout or until it encounters the arg string.
        #   this is necessary to pause program execution until we receive the prompt
        #   or else we'll send our command before the crestron dm-md is ready.
        # dump output to the debugger
        telnet_output = telnet.read_until(b">", timeout=2)
        cias_globals.debugger.message("TELN", "Telnet output: {}".format(telnet_output))

        # now send the actual command
        cias_globals.debugger.message("TELN", "Sending cmnd : {}".format(telnet_cmd))
        telnet.write(telnet_cmd.encode('ascii'))

        # read_until again, to capture any command output, in case it's useful
        telnet_output = telnet.read_until(b">", timeout=2)
        cias_globals.debugger.message("TELN", "Telnet output: {}".format(telnet_output))

        telnet.close()

    def lcd_update(self, message):
        # Combine the message with a separator and a tagline from the config file
        lcd_message = "{} {} {} {}".format(cias_globals.config['cias'].get('lcdHeader'),
                                           message,
                                           cias_globals.config['cias'].get('lcdSeparator'),
                                           cias_globals.config['cias'].get('lcdTagLine'))
        # Send it to the device LCD
        self.send_command("MESSage {}\r".format(lcd_message))

    def get_input_card_name(self, card_input):
        # return the pretty name of an input card
        return self.cardsInput[card_input-1][0]

    def route_av(self, card_input, card_output):
        # arrays are indexed on 0 (index 0 is the first), the args we pass in are indexed on 1 (card #1 is the first)
        # remove 1 from each
        card_input -= 1
        card_output -= 1

        # Build an lcd message line
        lcd_message = "{} > {}".format(self.cardsInput[card_input][0],
                                       self.cardsOutput[card_output][0])
        self.send_command("SETAVROUTE {} {}\r".format(self.cardsInput[card_input][1],
                                                      self.cardsOutput[card_output][1]))
        self.lcd_update(lcd_message)


# if __name__ == "__main__":
#     cias = CiasControl()
#
#     # Route input 1 to output 1
#     cias.route_av(1, 1)
