#External Modules
import argparse
import sys
import re

#WeaPy modules
from modules.prettify.colours import colors

def set_arguments():
    
    option = argparse.ArgumentParser()
    
    option.add_argument('-u','--url', dest='url', help='URL of website')
    option.add_argument('--user', dest='user', help='Username to access website, optional')
    option.add_argument('--password', dest='password', help='Password to access website, optional')
    option.add_argument('-o','--output', dest='output', help='Prints source code to terminal screen', action='store_true')
    option.add_argument('-j','--javascript', dest='javascript', help='Prints javascript source code to terminal screen', action='store_true')
    option.add_argument('--css', dest='css', help='Prints css source code to terminal screen', action='store_true')
    option.add_argument('-s','--search', dest='search', help='Searches for links and directories in source code', action='store_true')
    option.add_argument('--comments', dest='comments', help='Searches for comments in source code', action='store_true')
    option.add_argument('-A','--all', dest='all', help='Does -o, -H, -s, -w , -v --comments', action='store_true')
    option.add_argument('-w','--webanalyser', dest='webanal', help='Analyses web technology using Wappalyzer',action = 'store_true')
    option.add_argument('-v','--verbose', dest='verbose', help='prints out cookie and header information', action= 'store_true')
    option.add_argument('--ctf', dest = 'ctf', help='for ctfs, searches source code for comments, passwords/flags', action= 'store_true')
    option.add_argument('-c','--cookie', dest='cookie', help='set cookie name and value. Usage is python dict ({name:value})')
    option.add_argument('-H','--header', dest='header', help='set modified header. Usage is python dict ({name:value})')
    option.add_argument('-X','--post', dest='post', help='Makes a post request.', action='store_true')
    option.add_argument('--xss', dest='xss', help='Scans website for XSS vulns.', action='store_true')
    option.add_argument('--debug', dest='debug', help='prints out args dictionary to help with development', action='store_true')

    arg = vars(option.parse_args())
    
    if not arg['url']:
        option.error('>> No URL given. Use -u or --url to provide URL. Use -h or --help for more info')
    
    return arg


def clean_dictionary(dictionary):

    for (key, val) in dictionary.items():
        if val == None:
            dictionary.update({key: False})
    
    return dictionary


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
    
    tld = ['.com','.co.uk','.edu','.io','.ac.uk','.html','.org','.app','.amazon',
           'level1','level2','level3','level4','level5','level6']

    check = [check for check in tld if check in url]

    if len(check) == 0:
        print(colours['WARNING'] + 'Unknown Top Level Domain' + colours['RESET'])

    return url

def clean(string_to_clean):
    
    key = re.findall(r'{.*?:', string_to_clean)
    val = re.findall(r':.*?}', string_to_clean)
    key = str(*key).strip(':').strip('{')
    val = str(*val).strip(':').strip('}')
    dictionary = {key:val}
    
    return dictionary
    

def arguments():
    
    set_args = set_arguments()
    args = clean_dictionary(set_args)
    url = clean_url(args['url'])

    if args['header'] != False: 
        header = clean(args['header'])

    else:
        header = args['header']

    if args['cookie'] != False: 
        cookie = clean(args['cookie'])
        
    else:
        cookie = args['cookie']

    args.update({'url':url, 'header':header, 'cookie':cookie})

    if args['debug'] == True:
        print(args)

    if args['all'] == True:
        args['output'] = True
        args['verbose'] = True

    return args