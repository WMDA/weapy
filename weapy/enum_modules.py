import re
from utils import colors

    
def bs4_output(text):
        
    from bs4 import BeautifulSoup
        
    colours = colors()
    
    '''
    Replaces unecessary <br /> tags with spaces and unecessary & tags with < or >
    '''

    line_break= re.sub(r'<br />','\n',text)
    tag_left= re.sub(r'&lt;','<',line_break)
    tag_right= re.sub(r'&gt;','>',tag_left)
    output= re.sub(r'&nbsp;',' ',tag_right)

    '''
    Uses beautiful soup to prettify the output
    '''
    soup = BeautifulSoup(output, features="lxml")
        
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
    
    text_filter = re.sub('<a','',text)

    unfiltered_links = re.findall(r'href="h.*?"[^\s-]',text_filter)

    filter_target =  [re.sub(r'target=.*','',link) for link in unfiltered_links]

    filter_ending_tag = [re.sub('</a>','',link) for link in filter_target]

    filter_tags = [link.replace(r'<.*>','') for link in filter_ending_tag]

    filter_links = [link.replace('href=','') for link in filter_tags]
   
    return(filter_links)

def file_search(text):
    
    file_type =['gif','txt','jpeg']
    
    files=[]
    
    for format in file_type:     
        file_list = re.findall(r'[A-Za-z0-9]*.{}'.format(format),text)
        
        for file in file_list:
            if file not in files:
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
