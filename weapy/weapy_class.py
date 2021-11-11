import requests
import sys
from utils import colors
import enum_modules as enum


class WeaPy:

    '''
    WeaPy main class. Calls functions based on arguments passed, assigns arguments to self parameter,
    makes get request to website along with header and cookie info. 
    '''

    def __init__(self,args):

        '''
        init function. Calls functions based on arguments

        Parameters
        ---------------
        self : self parameter
        args : dictionary of arguments

        Returns
        -----------------
        GET request to website with header info
        enum modules : optional 
        '''

        self.args(args)
        
        self.colours = colors()
        
        self.get(self.output)

        self.headers(self.req)

        if self.search == True:

            enum.search_page(self.req.text)

        if self.webanal == True:

            enum.webanalyzer_output(self.url)

        if self.ctf == True:

            enum.ctf_mode(self.req.text)

        if self.javascript ==True:

            enum.javascript_output(self.req.text)

        if self.css ==True:

            enum.css_output(self.req.text)

    def args(self,args):

        '''
        Assigns keywords to self parameter

        Parameters
        ---------------
        self : self parameter
        args : Python dictionary of arguments

        Returns
        ----------------
        arguments assigned to self parameter

        '''

        self.url = args['url']
        
        self.password = args['password']
        
        self.username = args['user']
        
        self.output = args['output']
        
        self.search = args['search']

        self.webanal = args['webanal']

        self.header = args['header']

        self.ctf = args['ctf']

        self.cookie = args['cookie']

        self.verbose = args['verbose']

        self.javascript = args['javascript']

        self.css = args['css']



    def get(self,output):
        
        try:
            self.req = requests.get(self.url,auth=(self.username,self.password),cookies=self.cookie, headers=self.header)
        
        except Exception:
            
            print(self.colours['WARNING'] + self.colours['BLINK'] + '\nCONNECTIVITY ERROR\n',self.colours['RESET'] + '\nUnable to connect to', self.colours['RED'] + self.url, 
            self.colours['RESET']+ '\nIs this a valid website?\nCheck your connectivity\n')
            
            sys.exit(1)
        
        if self.req.status_code == 200:
       
            print(self.colours['GREEN'] + f'\n{self.url} is responding\n' + self.colours['RESET'])
               
            if output==True:

                print(enum.bs4_output(self.req.text))

        else:
            print(self.colours['RED'] + f'{self.req.status_code} recieved from {self.url}'+ self.colours['RESET'])
        
    def headers(self,website):

        self.web_header = website.headers

        if self.verbose == True:

            enum.header_output(self.web_header)





