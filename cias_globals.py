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
config['DEFAULT'] = {'input1Name': 'Input 1 [1]',
                     'input1Card': 1,
                     'input2Name': 'Input 2 [2]',
                     'input2Card': 2,
                     'input3Name': 'Input 3 [3]',
                     'input3Card': 3,
                     'input4Name': 'Input 4 [4]',
                     'input4Card': 4,
                     'input5Name': 'Input 5 [5]',
                     'input5Card': 5,
                     'input6Name': 'Input 6 [6]',
                     'input6Card': 6,
                     'input7Name': 'Input 7 [7]',
                     'input7Card': 7,
                     'input8Name': 'Input 8 [8]',
                     'input8Card': 8,
                     'output1Name': 'Output 1 [1]',
                     'output1Card': 17,
                     'output2Name': 'Output 2 [2]',
                     'output2Card': 18,
                     'output3Name': 'Output 3 [3]',
                     'output3Card': 19,
                     'output4Name': 'Output 4 [4]',
                     'output4Card': 20,
                     'output5Name': 'Output 5 [5]',
                     'output5Card': 21,
                     'output6Name': 'Output 6 [6]',
                     'output6Card': 22,
                     'output7Name': 'Output 7 [7]',
                     'output7Card': 23,
                     'output8Name': 'Output 8 [8]',
                     'output8Card': 24,
                     'lcdTagLine': 'Crestron AV',
                     'lcdSeparator': '__________________________',
                     'lcdHeader': 'Now showing'}

# Create a ['tto'] section containing the above defaults:
config['cias'] = {}

# Load the config file values overtop of the defaults above:
config_file_load("cias.cfg")

