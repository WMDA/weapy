#External Modules
from http.client import FOUND
import re
import requests

#Modules from WeaPy
from modules.prettify.colours import colors
import modules.enumerate.enum as enum 
import modules.enumerate.search as search

'''
This is the enumerate modules output.

Most of WeaPy enumerates logic happens in the enum_modules while 
enum handles making the output look cooleo.
'''

def bs4_output(request:str) -> str:

    '''
    Prettifys and adds colour to BeautifulSoup output.

    Parameters
    ----------
    Request:str HTML source code from requests module

    Returns
    -------
    final_output:str Output from Beautiful Soup's prettify with coloured source code.

    '''

    colours = colors()
    soup = enum.bs4_parse(request)
    pretty = soup.prettify()
    color_beg = re.sub(r'<', colours['PURPLE'] + '<' + colours['GREEN'], pretty)
    final_output = re.sub(r'>', colours['PURPLE'] + '> '+ colours['RESET'], color_beg)
      
    return final_output

    
def search_page(text:str):

    '''
    Prints to terminal all of the links, files and dirs found in coloured format


    Paramters
    ---------
    Request (str): HTML source code from requests module


    Returns
    --------
    output_links:list coloured list of links found in page (prints to terminal).
    output_dirs:list coloured list of dirs found in page (prints to terminal).
    files_in_page: list coloured list of files found in page (prints to terminal).

    '''
        
    colours = colors()
    files = search.file_search(text)
    files_in_page = [colours['BLUE'] + file + colours['RESET'] for file in files]
    output_dirs = search.dirs_search(text)
    links = enum.links_search(text)
    output_links = [colours['BLUE'] + link.replace('"','') + colours['RESET'] for link in links]
    
    print(colours['LIGHT_CYAN'] + colours['BOLD'] + '\nFiles found in page:\n' + colours['RESET'])
    print(*files_in_page, sep='\n')
    print(colours['LIGHT_CYAN'] + colours['BOLD'] + '\nDirs found in page:\n' + colours['RESET'])
    
    common_dirs = ['/js','/wechall', '/jquery', '/css','/html','/W3C','/DTD','/EN']
    
    for dir in output_dirs:
        if dir not in common_dirs:
            print(colours['LIGHT_GREEN'] + dir + colours['RESET'])
        else:
            print(colours['BLUE'] + dir + colours['RESET'])

    print(colours['BLUE'] + colours['BOLD'] + '\nLinks found:\n' + colours['RESET'])
    print(*output_links, sep='\n')
    

def webanalyzer_output(url:str):

    '''
    Prints to terminal all of the backend technology found in webpage. 
    Utilizes Wappalyzer for python

    Paramters
    ---------
    URL (str): Webpage URL

    Returns
    -------
    techno:list of dictionary items: Coloured list of dictionary items of backend category, name and version

    '''

    webanalyser = enum.webanalyzer(url)
    colours = colors()
    print(colours['LIGHT_CYAN'] + '\nFound the following web technologys:\n' + colours['BLUE'])
    
    for techno in webanalyser:
        print(*techno['Categories'], ':', techno['name'], *techno['version'])

    print('\n' + colours['RESET'])


def header_output(website_headers:requests.models.Response):
    
    '''
    Function to print header information to terminal in colour.
    Also sets cookie info as a different color

    Parameters
    ----------
    website_headers:requests.models.Response Request reponse.

    Returns
    -------
    Header information (prints to termnial)
    '''

    colours = colors()
    print(colours['PURPLE'] + colours['BOLD'] + '\nHeader and Set Cookie info\n' + colours['RESET'])

    for header_key, header_value in website_headers.items():
        if r'Set-Cookie' in header_key:
            print(colours['YELLOW'] + header_key + colours['RESET'], colours['PURPLE'] + header_value + colours['RESET'])
        else:
            print(header_key, header_value)

def ctf_mode(website_code):
    
    '''
    Work in progress function
    '''
    enum.passwords(website_code)
    enum.comments(website_code)
    enum.flags(website_code)


def javascript_output(text:str):

    '''
    Prints .js files to terminal.
    Needs further work
    '''

    colours = colors
    js_links= enum.javascript_links(text)

    for js in js_links:
        js = re.sub(r'"', '', js)

        try:
            js_page = requests.get(js)
            print(js)
            print(js_page.text)

        except:
            print(js)
            print(colours['RED'] +'Unable to open page' + colours['RESET']) 

def css_output(text:str):

    '''
    Prints .js files to terminal.
    Needs further work
    '''

    css_link= enum.css_links(text)

    for css in css_link:
        css = re.sub(r'"', '', css)

        try:
            css_page = requests.get(css)
            print(css)
            print(css_page.text)

        except:
            print(css)
            print('Unable to open page')

def found_form(source_code:str):
    
    '''
    Prints out to console any form details

    Parameters
    ----------
    source_code:str website source code
    '''

    colours = colors()
    form = enum.find_input_forms(source_code)
    
    if form != None:
        print(colours['CYAN'] + 'Found form:\n' + colours['RESET'])
        cleaned_form = re.sub('<br/>', '', str(form))
        print(colours['LIGHT_GREEN'] + cleaned_form + colours['RESET'], '\n')
    
    else:
        print(colours['RED'] + 'No forms found:\n' + colours['RESET'])
