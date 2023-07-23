""" cias_globals - program globals for cias

So I can have program settings that hopefully don't end up in github

Requirements
------------
configparser : Basic config language parser
cias_debugger : Error and info message handler

"""

from configparser import ConfigParser
from cias_debugger import CiasDebugger

debugger = CiasDebugger()
config = ConfigParser()


def config_file_load(config_file):
    debugger.message("INFO", "Loading config file: {}".format(
        config_file))
    config.read(config_file)
    debugger.message("INFO", "Config Sections: {}".format(
        config.sections()))
    for cay in config['cias']:
        debugger.message("INFO", "    Key: {}, Value: {}".format(
            cay, config['cias'][cay]))


# These defaults apply unless overridden in the config file ['cias'] section:
config['DEFAULT'] = {'c1hostname':   'hostname_or_ip.com',
                     'c1input1Name': 'Input 1 [1]',
                     'c1input1Card': 1,
                     'c1input2Name': 'Input 2 [2]',
                     'c1input2Card': 2,
                     'c1input3Name': 'Input 3 [3]',
                     'c1input3Card': 3,
                     'c1input4Name': 'Input 4 [4]',
                     'c1input4Card': 4,
                     'c1input5Name': 'Input 5 [5]',
                     'c1input5Card': 5,
                     'c1input6Name': 'Input 6 [6]',
                     'c1input6Card': 6,
                     'c1input7Name': 'Input 7 [7]',
                     'c1input7Card': 7,
                     'c1input8Name': 'Input 8 [8]',
                     'c1input8Card': 8,
                     'c1output1Name': 'Output 1 [1]',
                     'c1output1Card': 17,
                     'c1output2Name': 'Output 2 [2]',
                     'c1output2Card': 18,
                     'c1output3Name': 'Output 3 [3]',
                     'c1output3Card': 19,
                     'c1output4Name': 'Output 4 [4]',
                     'c1output4Card': 20,
                     'c1output5Name': 'Output 5 [5]',
                     'c1output5Card': 21,
                     'c1output6Name': 'Output 6 [6]',
                     'c1output6Card': 22,
                     'c1output7Name': 'Output 7 [7]',
                     'c1output7Card': 23,
                     'c1output8Name': 'Output 8 [8]',
                     'c1output8Card': 24,
                     'c1lcdTagLine': 'Crestron AV',
                     'c1lcdSeparator': '__________________________',
                     'c1lcdHeader': 'Now showing'}

# Create a ['tto'] section containing the above defaults:
config['cias'] = {}

# Load the config file values overtop of the defaults above:
config_file_load("cias.cfg")

