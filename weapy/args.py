import argparse

def arguments():
    option=argparse.ArgumentParser()
    option.add_argument('-u','--url',dest='url',help='URL of website')
    option.add_argument('--user',dest='user',help='Username to access website, optional')
    option.add_argument('--pass',dest='pass',help='Password to access website, optional')
    option.add_argument('-p','--print',dest='print',help='Prints source code to terminal screen')
    arguments=option.parse_args()
    if not arguments.url:
        option.error('>> No URL given. Use -u or --url to provide URL. Use -h / --help for more info')
    return arguments


