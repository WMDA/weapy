import argparse

def arguments():
    option=argparse.ArgumentParser()
    option.add_argument('-u','--url',dest='url',help='URL of website')
    option.add_argument('--user',dest='user',help='Username to access website, optional')
    option.add_argument('-p','--password',dest='password',help='Password to access website, optional')
    option.add_argument('-o','--output',dest='output',help='Prints source code to terminal screen', action='store_true')
    
    arguments=option.parse_args()
    
    if 'http' or 'https' in arguments.url:
        arguments.url = 'http://www.' + arguments.url

    if not arguments.url:
        option.error('>> No URL given. Use -u or --url to provide URL. Use -h / --help for more info')
    
    return arguments


