import re

from pkg_resources import empty_provider
from utils import colors
from bs4 import BeautifulSoup

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

def bs4_output(request):

    colours = colors()
    soup= bs4_parse(request)
    pretty = soup.prettify()
    '''
    Finds all the tags and changes what is inside the tags to purple 
    and the rest white.
    '''
    color_beg= re.sub(r'<', colours['PURPLE'] + '<' + colours['GREEN'],pretty)
       
    final_output= re.sub(r'>', colours['PURPLE'] + '> '+ colours['RESET'], color_beg)
      
    return(final_output)

def dirs_search(text):

    remove_ending_tags = re.sub(r'</.*?>','',text)

    dir_list = re.findall(r'/[A-Za-z0-9\.]*', remove_ending_tags)

    filter_no_dir = [dir for dir in dir_list if len(dir) > 1]

    filter_links = [dir for dir in filter_no_dir if '.' not in dir ]

    dirs = list(set(filter_links))
        
    return(dirs)

def links_search(text): 

   page = bs4_output(text)
   
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

    
def search_page(text):
        
    colours = colors()

    print('\nSearching for Files Dirs and Links on page\n')

    files = file_search(text)

    files_in_page = [colours['LIGHT_CYAN'] + file + colours['RESET'] for file in files]

    dirs = dirs_search(text)
        
    output_dirs = [colours['LIGHT_GREEN'] + dir + colours['RESET'] for dir in dirs]
      
    links = links_search(text)
        
    output_links = [colours['LIGHT_PURPLE'] + link.replace('"','') + colours['RESET'] for link in links]

    print(colours['PURPLE'] + colours['BOLD'] + '\nFiles found in page:\n' + colours['RESET'])

    print(*files_in_page,sep='\n')

    print(colours['YELLOW'] + colours['BOLD'] + '\nDirs found in page:\n' + colours['RESET'])

    print(*output_dirs,sep='\n')

    print(colours['BLUE'] + colours['BOLD'] + '\nLinks found:\n'+  colours['RESET'])

    print(*output_links,sep='\n')
    
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

def webanalyzer_output(url):
    
    webanalyser = webanalyzer(url)
    
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

def javascript_output(text):

    import requests

    js_links= javascript_links(text)

    for js in js_links:
        js = re.sub(r'"','',js)

        try:
            
            js_page = requests.get(js)

            print(js)
            print(js_page.text)

        except:
            print(js)
            print('Unable to open page') 

def css_output(text):

    import requests

    css_link= css_links(text)

    for css in css_link:
        css = re.sub(r'"','',css)

        try:
            
            css_page = requests.get(css)
            print(css)
            print(css_page.text)

        except:
            print(css)
            print('Unable to open page')

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
    

def input_forms(request):
        
        colours =colors()
        
        forms = find_input_forms(request)
        form_details = get_form_details(forms)


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


            
    
    


