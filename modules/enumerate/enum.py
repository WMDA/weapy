#External Modules
from distutils.command.upload import upload
from bs4 import BeautifulSoup
import re

from matplotlib.pyplot import flag
from Wappalyzer import Wappalyzer, WebPage
import warnings

#WeaPy Modules
from modules.prettify.colours import colors

'''
WeaPys enumerate modules
'''
    
def bs4_parse(request):
    
    '''
    Replaces unecessary <br /> tags with spaces and unecessary & tags with < or >
    '''

    line_break= re.sub(r'<br />', '\n', request)
    tag_left= re.sub(r'&lt;', '<', line_break)
    tag_right= re.sub(r'&gt;', '>', tag_left)
    output= re.sub(r'&nbsp;', ' ', tag_right)

    '''
    Uses beautiful soup to prettify the output
    '''
    soup = BeautifulSoup(output, features="lxml")
    
    return soup

def webanalyzer(url):

    # Wappalyzer throws up unbalanced parentheses warnings
    warnings.filterwarnings('ignore')
    wappalyzer = Wappalyzer.latest()
        
    # Create webpage
        
    webpage = WebPage.new_from_url(url)
        
    # analyze
        
    results = wappalyzer.analyze_with_versions_and_categories(webpage)
    
    technology =[]
    
    for tech_key, tech_val in results.items():
            techno_dict={'Categories': tech_val['categories'], 'name':tech_key, 'version':tech_val['versions']}    
            if techno_dict not in technology:
                technology.append(techno_dict)

    return technology

def passwords(website_code):

    colours = colors()
    passwords = re.findall('password[\w\s.].*', website_code)
    
    if len(passwords) >0:
        print(colours['BLINK'] + colours['YELLOW'] + colours['BOLD'] +
        'POTENTIAL PASSWORDS FOUND!!' + colours['RESET'] + colours['BOLD'])
         
        print(*passwords, sep='\n')
    
    else:
        print(colours['WARNING'] + 'NO PASSWORDS FOUND')

def flags(website_code):
    colours = colors()
    flags = re.findall('...{.*}', website_code)
    
    if len(flags) >0:
        print(colours['BLINK'] + colours['CYAN'] + colours['BOLD'] +
        'POTENTIAL FLAGS FOUND!!' + colours['RESET'] + colours['BOLD'])
        print(*flags, sep='\n')
    
    else:
        print(colours['WARNING'] + 'NO FLAGS FOUND')

def comments(website_code):

    colours = colors()
    comments = re.findall(r'<!.*>', website_code)
    print(colours['CYAN']+ '\nFound Comments on the page' + colours['RESET'])
    print(colours['LIGHT_GREEN'] + '\n', *comments, sep='\n')
    print(colours['RESET'] + '\n') 

def links_search(text): 

   soup = bs4_parse(text)
   page = soup.prettify()
   html_links = re.findall(r'(http.*//.*?[^\'"><]+)', page)

   return html_links

def javascript_links(text):
    
    links = links_search(text)
    java_script = [js for js in links if '.js' in js]
    return java_script

def css_links(text):
        
    links = links_search(text)
    css = [css for css in links if '.css' in css]
    return css


def find_input_forms(request):

    soup = bs4_parse(request)
    forms = soup.find('form')
    return forms

def get_form_details(form):
    
    details = {}
    # get the form action (requested URL)
    action = form.get("action")
    method = form.attrs.get("method", "get")
    
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        input_value =input_tag.attrs.get("value", "")
        inputs.append({"type": input_type, "name": input_name, "value": input_value})
    
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs

    return details

def input_forms(request, *submit_value, vulns=False):

    '''
    Work in progress. Functionally works however function may need to be split up.
    '''
        
    colours = colors()
    forms = find_input_forms(request)
    form_details = get_form_details(forms)

    for val in form_details['inputs']:
        if val['type'] != 'submit':
            if val['value'] == '':
                if vulns == False:
                    print(colours['YELLOW'] + f'>> Enter value for {val["name"]}' + colours['RESET'])
                    value=input()
                
                else:
                    value = submit_value

                val['value'] = value

        elif val['type'] == 'submit':
            if val['value'] == '':
                val['value'] == 'submit'
        
    return form_details