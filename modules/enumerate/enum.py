#External Modules
from bs4 import BeautifulSoup
import re

#WeaPy Modules
from modules.prettify.colours import colors

'''
WeaPys enumerate modules
'''
    
def bs4_parse(request):
    
    '''
    Replaces unecessary <br /> tags with spaces and unecessary & tags with < or >
    '''

    line_break= re.sub(r'<br />','\n',request)
    tag_left= re.sub(r'&lt;','<',line_break)
    tag_right= re.sub(r'&gt;','>',tag_left)
    output= re.sub(r'&nbsp;',' ',tag_right)

    '''
    Uses beautiful soup to prettify the output
    '''
    soup = BeautifulSoup(output, features="lxml")
    
    return (soup)  

def dirs_search(text):

    remove_ending_tags = re.sub(r'</.*?>','',text)

    dir_list = re.findall(r'/[A-Za-z0-9\.]*', remove_ending_tags)

    filter_no_dir = [dir for dir in dir_list if len(dir) > 1]

    filter_links = [dir for dir in filter_no_dir if '.' not in dir ]

    dirs = list(set(filter_links))
        
    return(dirs)

def links_search(text): 

   soup = bs4_parse(text)

   page = soup.prettify()
   
   html_links = re.findall(r'(http.*//.*?[^\'"><]+)',page)

   return(html_links)


def file_search(text):
    
    file_type =['gif','txt','jpeg','html']
    
    files=[]
    
    for format in file_type:     
        file_list = re.findall(r'[A-Za-z0-9-]*.{}'.format(format),text)
        
        for file in file_list:
            if file not in files:
                if '.'in file:
                    files.append(file)

    return(files)


def webanalyzer(url):

    from Wappalyzer import Wappalyzer, WebPage
        
    import warnings
        
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

    return(technology)

def ctf_mode(website_code):

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
        print(colours['WARNING'] + 'NO PASSWORDS FOUND')

def javascript_links(text):
    
    links= links_search(text)

    java_script = [js for js in links if '.js' in js]

    return(java_script)

def css_links(text):
        
    links= links_search(text)

    css = [css for css in links if '.css' in css]

    return(css)


def find_input_forms(request):
    soup = bs4_parse(request)
    forms = soup.find('form')
    return(forms)

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
    return (details)
    