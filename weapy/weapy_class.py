# External Modules 
import requests
import sys

# WeaPy modules
from modules.prettify.colours import colors
import modules.prettify.enum_output as enum
from modules.http_requests.http_request import HTTPRequests


class WeaPy:

    '''
    WeaPy standalone main calss. Calls functions based on arguments passed, assigns arguments to self parameter,
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

        self.http_request= HTTPRequests(args)

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

            self.http_request.post()

        

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
        