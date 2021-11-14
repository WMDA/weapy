#External Modules
import re
import requests

#Modules from WeaPy
from modules.prettify.colours import colors
from modules.enumerate import enum 

'''
This is the enumerate modules output.

Most of WeaPy enumerates logic happens in the enum_modules while enum handles making the output look cooleo.
'''

def bs4_output(request):

    '''
    Prettifys and adds colour to BeautifulSoup output.

    Parameters
    ----------------------------------------------
    Request (str): HTML source code from requests module

    Returns
    ----------------------------------------------
    final_output (str) : Output from Beautiful Soup's prettify with coloured source code.

    '''

    colours = colors()

    soup= enum.bs4_parse(request)

    pretty = soup.prettify()

    color_beg= re.sub(r'<', colours['PURPLE'] + '<' + colours['GREEN'],pretty)
       
    final_output= re.sub(r'>', colours['PURPLE'] + '> '+ colours['RESET'], color_beg)
      
    return(final_output)

    
def search_page(text):

    '''
    Prints to terminal all of the links, files and dirs found in coloured format


    Paramters
    ---------------------------------
    Request (str): HTML source code from requests module


    Returns
    ----------------------------------
    output_links (list): coloured list of links found in page (prints to terminal).
    output_dirs (list): coloured list of dirs found in page (prints to terminal).
    files_in_page (list): coloured list of files found in page (prints to terminal).

    '''
        
    colours = colors()

    print('\nSearching for Files Dirs and Links on page\n')

    files = enum.file_search(text)

    files_in_page = [colours['LIGHT_CYAN'] + file + colours['RESET'] for file in files]

    dirs = enum.dirs_search(text)
        
    output_dirs = [colours['LIGHT_GREEN'] + dir + colours['RESET'] for dir in dirs]
      
    links = enum.links_search(text)
        
    output_links = [colours['LIGHT_PURPLE'] + link.replace('"','') + colours['RESET'] for link in links]

    print(colours['PURPLE'] + colours['BOLD'] + '\nFiles found in page:\n' + colours['RESET'])

    print(*files_in_page,sep='\n')

    print(colours['YELLOW'] + colours['BOLD'] + '\nDirs found in page:\n' + colours['RESET'])

    print(*output_dirs,sep='\n')

    print(colours['BLUE'] + colours['BOLD'] + '\nLinks found:\n'+  colours['RESET'])

    print(*output_links,sep='\n')
    

def webanalyzer_output(url):

    '''
    Prints to terminal all of the backend technology found in webpage. Utilizes Wappalyzer for python


    Paramters
    ---------------------------------
    URL (str): Webpage URL


    Returns
    ----------------------------------

    techno (list of dictionary items): Coloured list of dictionary items of backend category, name and version


    '''
        
    
    webanalyser = enum.webanalyzer(url)
    
    colours = colors()
    
    print(colours['LIGHT_CYAN'] + '\nFound the following web technologys:\n' + colours['BLUE'])
    
    for techno in webanalyser:
        print(*techno['Categories'],':', techno['name'],*techno['version'])

    print('\n' + colours['RESET'])


def header_output(website_headers):

    colours = colors()

    print(colours['PURPLE'] + colours['BOLD'] + '\nHeader and Set Cookie info\n' + colours['RESET'])

    for header_key, header_value in website_headers.items():
        
        if r'Set-Cookie' in header_key:
            print(colours['BLINK'] + colours['YELLOW'] + header_key + colours['RESET'], colours['PURPLE'] + header_value + colours['RESET'])

        else:
            print(header_key, header_value)

def ctf_mode(website_code):

    '''
    Work in progress. May move from enumerate modules. Functionally Works but function may need to be split up
    '''
    colours = colors()
    
    passwords = re.findall('password[\w\s.].*', website_code)
    
    further_search_text = re.sub(r'<.*>','',website_code)

    #HTTP/HTTPS links will always come back as a false positive. So needs to be sub out
    sub_out_http = re.sub(r'http.*:','',further_search_text)

    further_search = re.findall(r'.*:.*', sub_out_http)

    passwords = passwords + further_search
    
    if len(passwords) >0:
        print(colours['BLINK'] + colours['YELLOW'] + colours['BOLD'] +
        'POTENTIAL PASSWORDS FOUND!!' + colours['RESET'] + colours['BOLD'])
         
        print(*passwords, sep='\n')
    
    else:
        print(colours['RED'] + 'NO PASSWORDS FOUND' + colours['RESET'])

def javascript_output(text):

    '''
    Prints .js files to terminal.
    Needs further work
    '''

    colours = colors

    js_links= enum.javascript_links(text)

    for js in js_links:
        js = re.sub(r'"','',js)

        try:
            
            js_page = requests.get(js)

            print(js)
            print(js_page.text)

        except:
            print(js)
            print(colours['RED'] +'Unable to open page' + colours['RESET']) 

def css_output(text):

    '''
    Prints .js files to terminal.
    Needs further work
    '''



    css_link= enum.css_links(text)

    for css in css_link:
        css = re.sub(r'"','',css)

        try:
            
            css_page = requests.get(css)
            print(css)
            print(css_page.text)

        except:
            print(css)
            print('Unable to open page')

def input_forms(request):

    '''
    Work in progress. Functionally works however function may need to be split up.
    '''
        
    colours =colors()
        
    forms = enum.find_input_forms(request)
    form_details = enum.get_form_details(forms)


    for val in form_details['inputs']:
        if val['type'] !='submit':
            if val['value'] =='':
                print(colours['YELLOW'] + f'>> Enter value for {val["name"]}' + colours['RESET'])
                value=input()
                val['value'] = value

        elif val['type'] == 'submit':
            if val['value'] =='':
                val['value'] ='submit'
        
    return(form_details)