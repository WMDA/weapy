import argparse

def arguments():
    option=argparse.ArgumentParser()
    option.add_argument('-u','--url',dest='url',help='URL of website')
    option.add_argument('--user',dest='user',help='Username to access website, optional')
    option.add_argument('-p','--password',dest='password',help='Password to access website, optional')
    option.add_argument('-o','--output',dest='output',help='Prints source code to terminal screen', action='store_true')
    option.add_argument('-s','--search',dest='search',help='Searches for links and directories in source code', action='store_true')
    
    arguments=option.parse_args()
    
    if not arguments.url:

        option.error('>> No URL given. Use -u or --url to provide URL. Use -h / --help for more info')

    if ('http://www.' or 'https://www.') not in arguments.url:

        arguments.url = 'http://www.' + arguments.url
        
        return arguments
        
    
    else:
        
        return arguments


def colors():
    colors= {
    'HEADER' :'\033[95m',
    'BLUE' : '\033[94m',
    'CYAN' : '\033[96m',
    'GREEN' : '\033[92m',
    'WARNING' : '\033[93m',
    'FAIL' : '\033[91m',
    'RESET' : '\033[0m',
    'BLACK' : "\033[0;30m",
    'RED' :  '\033[0;31m',
    'GREEN' : "\033[0;32m",
    'BROWN' : "\033[0;33m",
    'BLUE' : "\033[0;34m",
    'PURPLE' : "\033[0;35m",
    'LIGHT_GRAY' : "\033[0;37m",
    'DARK_GRAY' : "\033[1;30m",
    'LIGHT_RED' : "\033[1;31m",
    'LIGHT_GREEN' : "\033[1;32m",
    'YELLOW' : "\033[1;33m",
    'LIGHT_BLUE' : "\033[1;34m",
    'LIGHT_PURPLE' : "\033[1;35m",
    'LIGHT_CYAN' : "\033[1;36m",
    'LIGHT_WHITE' : "\033[1;37m",
    'BOLD' : "\033[1m",
    'FAINT' : "\033[2m",
    'ITALIC': "\033[3m",
    'UNDERLINE' : "\033[4m",
    'BLINK' : "\033[5m",
    'NEGATIVE' : "\033[7m",
    'CROSSED' : "\033[9m",
    }

    return colors



