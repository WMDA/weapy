# External Modules 
import sys

# WeaPy modules
from modules.prettify.colours import colors
import modules.prettify.enum_output as enum
from modules.enumerate.enum import comments
from modules.enumerate.search import text
from modules.http_requests.http_request import HTTPRequests
from modules.file.file import url     

class WeaPy:

    '''
    WeaPy standalone main calss. Calls functions based on arguments passed, 
    assigns arguments to self parameter,makes get request to website along 
    with header and cookie info. 
    '''

    def __init__(self, args:dict):

        '''
        init function. Calls functions based on arguments
        
        Parameters
        ---------------
        self self parameter
        args:dict dictionary of arguments
        
        Returns
        -----------------
        GET request to website with header info
        enum modules : optional 
        '''

        self.args(args)

        if self.file !=False:
            url(self.file, self.url)
            sys.exit(0)

        try:
            self.http_request= HTTPRequests(args)

        except Exception:
            sys.exit(1)

        self.colours = colors()
        
        if self.search == True:
            enum.search_page(self.http_request.req.text)

        if self.webanal == True:
            enum.webanalyzer_output(self.url)

        if self.ctf == True:    
            enum.ctf_mode(self.http_request.req.text)

        if self.javascript ==True:
            enum.javascript_output(self.http_request.req.text)

        if self.css ==True:
            enum.css_output(self.http_request.req.text)

        if self.data != False:
            self.http_request.post(self.url)
        
        if self.all == True:
            try:
                enum.webanalyzer_output(self.url)

            except: 
                print(self.colours['RED'] + '\nUnable to determine backend technology. Most likely a time out issue'+ self.colours['RESET'])

            enum.search_page(self.http_request.req.text)
            comments(self.http_request.req.text)

        if self.comments == True:
            comments(self.http_request.req.text)

        if self.text != False:
            text(self.http_request.req.text, self.text)

        if self.forms == True:
            enum.found_form(self.http_request.req.text)


    def args(self, args:dict):

        '''
        Assigns keywords to self parameter
        
        Parameters
        ---------------
        self parameter
        args:dict dictionary of arguments
        
        Returns
        ----------------
        arguments assigned to self parameter

        TODO make this cleaner as at the moment is redudant
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
        self.data = args['post']
        self.all = args['all']
        self.comments = args['comments']
        self.text = args['text']
        self.forms = args['forms']
        self.file = args['file']