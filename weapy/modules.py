import requests
import sys
import re
from utils import colors


class Weapy:

    def __init__(self,args):
        
        self.args(args)
        
        self.colours = colors()
        
        self.host(self.output)

        print(self.req.cookies.get_dict())

        if self.search == True:

            self.search_page(self.req.text)

        if self.webanal == True:

            self.webanalyzer(self.url)

    def args(self,args):

        '''
        Assigns keywords to self parameter
        
        '''

        self.url = args['url']
        
        self.password = args['password']
        
        self.username = args['user']
        
        self.output = args['output']
        
        self.search = args['search']

        self.webanal = args['webanal']

    def host(self,output):
        
        try:
            self.req = requests.get(self.url,auth=(self.username,self.password))
        
        except Exception:
            
            print(self.colours['WARNING'] + self.colours['BLINK'] + '\nCONNECTIVITY ERROR\n',self.colours['RESET'] + '\nUnable to connect to', self.colours['RED'] + self.url, 
            self.colours['RESET']+ '\nIs this a valid website?\nCheck your connectivity\n')
            
            sys.exit(1)
        
        if self.req.status_code == 200:
       
            print(self.colours['GREEN'] + f'\n{self.url} is responding\n' + self.colours['RESET'])
               
            
            if output==True:
                print(self.bs4_output(self.req.text))

        else:
            print(self.colours['RED'] + f'{self.req.status_code} recieved from {self.url}'+ self.colours['RESET'])

    def bs4_output(self,text):
        
        from bs4 import BeautifulSoup
        
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
        
        pretty= soup.prettify()
        
        '''
        Finds all the tags and changes what is inside the tags to purple 
        and the rest white.
        '''
        color_beg= re.sub(r'<', self.colours['PURPLE'] + '<' + self.colours['GREEN'],pretty)
        
        final_output= re.sub(r'>', self.colours['PURPLE'] + '> '+ self.colours['RESET'], color_beg)
        
        return(final_output)

    def dirs_search(self,text):

        remove_ending_tags = re.sub(r'</.*?>','',text)

        dir_list = re.findall(r'/[A-Za-z0-9\.]*', remove_ending_tags)

        filter_no_dir = [dir for dir in dir_list if len(dir) > 1]

        filter_links = [dir for dir in filter_no_dir if '.' not in dir ]

        dirs = list(set(filter_links))
        
        return(dirs)

    def links_search(self,text):
        
        text_filter = re.sub('<a','',text)

        unfiltered_links = re.findall(r'href="h.*?"[^\s-]',text_filter)

        filter_target =  [re.sub(r'target=.*','',link) for link in unfiltered_links]

        filter_ending_tag = [re.sub('</a>','',link) for link in filter_target]

        filter_tags = [link.replace(r'<.*>','') for link in filter_ending_tag]

        filter_links = [link.replace('href=','') for link in filter_tags]

        
        return(filter_links)

    def search_page(self, text):
        
        print('\nSearching for dirs and Links on page\n')

        dirs = self.dirs_search(text)
        
        output_dirs = [self.colours['LIGHT_GREEN'] + dir + self.colours['RESET'] for dir in dirs]
        
        links = self.links_search(text)
        
        output_links = [self.colours['LIGHT_PURPLE'] + link.replace('"','') + self.colours['RESET'] for link in links]

        print(self.colours['YELLOW'] + self.colours['BOLD'] + '\nDirs found in page:\n' + self.colours['RESET'])

        print(*output_dirs,sep='\n')

        print(self.colours['BLUE'] + self.colours['BOLD'] + '\nLinks found:\n'+ self.colours['RESET'])

        print(*output_links,sep='\n')
    
    def webanalyzer(self,url):

        from Wappalyzer import Wappalyzer, WebPage
        
        import warnings
        
        # Wappalyzer throws up unbalanced parentheses warnings
        warnings.filterwarnings('ignore')
        
        wappalyzer = Wappalyzer.latest()
        
        # Create webpage
        
        webpage=WebPage.new_from_url(url)
        
        # analyze
        
        results = wappalyzer.analyze_with_categories(webpage)

        technology = [self.colours['BLUE'] + tech + self.colours['RESET'] for tech in results.keys()]
        
        print(self.colours['LIGHT_CYAN'] + '\nFound the following web technologys:\n' + self.colours['RESET'])
        print(*technology,sep='\n')


    def cookie_manipulator(self,cookie):
        session_cookies = self.req.cookies
        #cookies=cookie
        #self.req=requests.get(self.url,auth=(self.username,self.password),cookies=cookie)