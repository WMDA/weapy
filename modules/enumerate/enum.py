#External Modules
from distutils.command.upload import upload
from bs4 import BeautifulSoup
import re
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

def dirs_search(text):

    remove_ending_tags = re.sub(r'</.*?>', '', text)
    remove_html_links = re.sub(r'(http.*//.*?[^\'"><]+)','', remove_ending_tags)
    dir_list = re.findall(r'/[A-Za-z0-9_\.]*', remove_html_links)
    
    
    further_search = re.findall(r'.*?/.*?', remove_html_links)
    further_search_results = [re.sub(r'<.*?=','', dir) for dir in further_search]
    
    common_dirs =['files','uploads', 'images']
    strip = [dirs.lstrip('/"').rstrip('/') for dirs in further_search_results]
    results = [dirs for dirs in strip if dirs in common_dirs]

    filter_no_dir = [dir for dir in dir_list if len(dir) > 1]
    filter_links = [dir for dir in filter_no_dir if '.' not in dir]
    dirs = filter_links + results
    dirs = list(set(dirs))

    return dirs

def links_search(text): 

   soup = bs4_parse(text)
   page = soup.prettify()
   html_links = re.findall(r'(http.*//.*?[^\'"><]+)', page)

   return html_links


def file_search(text):
    
    file_type = ['gif','txt','jpeg','html','py','png']
    files = []
    
    for format in file_type:     
        file_list = re.findall(r'[A-Za-z0-9-]*.{}'.format(format), text)
        
        for file in file_list:
            if file not in files:
                if '.'in file:
                    files.append(file)

    return files


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

def comments(website_code):

    colours = colors()
    comments = re.findall(r'<!.*>', website_code)
    print(colours['CYAN']+ '\nFound Comments on the page' + colours['RESET'])
    print(colours['LIGHT_GREEN'] + '\n', *comments, sep='\n')
    print(colours['RESET'] + '\n') 

def javascript_links(text):
    
    links= links_search(text)
    java_script = [js for js in links if '.js' in js]
    return java_script

def css_links(text):
        
    links= links_search(text)
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
        
    colours =colors()
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