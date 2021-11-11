import argparse
import sys
from utils import colors

def set_arguments():
    
    option = argparse.ArgumentParser()
    
    option.add_argument('-u','--url',dest='url',help='URL of website')
    
    option.add_argument('--user',dest='user',help='Username to access website, optional')
    
    option.add_argument('--password',dest='password',help='Password to access website, optional')
    
    option.add_argument('-o','--output',dest='output',help='Prints source code to terminal screen', action='store_true')
    
    option.add_argument('-s','--search',dest='search',help='Searches for links and directories in source code', action='store_true')

    option.add_argument('-w','--webanalyser', dest='webanal', help='Analyses web technology using Wappalyzer',action = 'store_true')

    option.add_argument('-v','--verbose',dest = 'verbose', help = 'prints out cookie and header information', action= 'store_true')

    option.add_argument('--ctf',dest = 'ctf', help = 'for ctfs, searches webpage for passwords/flags', action= 'store_true')

    option.add_argument('-c','--cookie',dest = 'cookie', help = 'set cookie name and value. Usage is python dict ({name:value})')

    option.add_argument('-H','--header',dest = 'header', help = 'set modified header. Usage is python dict ({name:value})',)
    
    arg = vars(option.parse_args())
    
    if not arg['url']:

        option.error('>> No URL given. Use -u or --url to provide URL. Use -h or --help for more info')
    
    return arg


def clean_dictionary(dictionary):

    for (key,val) in dictionary.items():
        if val == None:
            dictionary.update({key: False})
    
    return(dictionary)


def clean_url(url):
    
    colours = colors()

    if 'www.' not in url:

        if 'http' not in url:
            url = 'www.' + url

    if 'www.http' in url:
        print(colours['WARNING'] + f"Weird {url}, this won't work" + colours['RESET'])
        sys.exit(1)

    if 'http' not in url:
        url = 'http://' + url
    
    tld = ['.com','.co.uk','.edu','.io','.ac.uk','.html','.org']

    check = [check for check in tld if check in url]

    if len(check) == 0:

        print(colours['WARNING'] + 'No known Top Level Domain specified please specify in the URL')
        
        sys.exit(1)
    
    return(url)

def clean_header(header):
    print(header)

def arguments():
    
    set_args = set_arguments()

    args = clean_dictionary(set_args)

    url = clean_url(args['url'])

    #header = clean_header(args['header'])
    
    args.update({'url':url})

    return(args)
