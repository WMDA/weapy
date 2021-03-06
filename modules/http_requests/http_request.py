#External modules
import requests
import sys

#Weapy modules
import modules.prettify.enum_output as enum
import modules.enumerate.enum as enumerate
from modules.prettify.colours import colors

class HTTPRequests:

    def __init__(self, args:dict):

        self.colours = colors()
        self.args(args)

        try: 
            self.get(self.output)
            self.headers(self.req)

        except Exception:
            
            print(self.colours['WARNING'] + self.colours['BLINK'] + '\nCONNECTIVITY ERROR\n',self.colours['RESET'] + '\nUnable to connect to', 
            self.colours['RED'] + self.url, self.colours['RESET']+ '\nIs this a valid website?\nCheck your connectivity\n')

    def args(self, args:dict):

        '''
        Assigns keywords to self parameter
        Parameters
        ---------------
        self : self parameter
        args : Python dictionary of arguments
        Returns
        ----------------
        arguments assigned to self parameter

        TODO make this cleaner as is a lot of redundant info and is repeat in WeaPY class
        '''

        self.url = args['url']
        self.password = args['password']
        self.username = args['user']
        self.output = args['output']
        self.header = args['header']
        self.cookie = args['cookie']
        self.verbose = args['verbose']

    def get(self, output:bool):

        '''
        Function to make get requests

        Parameters
        ----------
        self parameter
        output:bool argument to print output to terminal
        
        Returns
        -------
        Get request
        '''
        
        self.req = requests.get(self.url, auth=(self.username, self.password), cookies=self.cookie, headers=self.header)
               
        if self.req.status_code == 200:         
            print(self.colours['GREEN'] + f'\n{self.url} is responding\n' + self.colours['RESET'])

            if output == True:
                print(enum.bs4_output(self.req.text))
                    
        else:
            print(self.colours['RED'] + f'{self.req.status_code} recieved from {self.url}' + self.colours['RESET'])

        
    def headers(self, website:requests.models.Response):

        '''
        Function to get header information from response.

        Parameters
        ----------
        self parameter
        website:requests.models.Response Request response.

        Returns
        -------
        '''

        self.web_header = website.headers

        if self.verbose == True:
            enum.header_output(self.web_header)

    def post(self):

        '''
        Function to make post request.

        Parameters
        ----------
        None

        Returns
        -------
        Post request.
        '''
        
        form_data = enumerate.input_forms(self.req.text)

        data ={}

        for input in form_data['inputs']:
            data[input['name']] = input['value']


        if form_data['method'].lower() == 'post':    
            try:
                self.req_post = requests.post(self.url, data=data, auth=(self.username, self.password))
                
                if self.req_post.status_code == 200:
                    print(enum.bs4_output(self.req_post.text))

                else:
                    print(self.colours['WARNING'] + 'Unable to make Post request'  + self.colours['RESET'])
                    sys.exit(1)
                
            except Exception:
                print(self.colours['WARNING'] + 'Unable to Post!!!' + self.colours['RESET'])
                sys.exit(1)

        elif form_data['method'].lower() =='get':

            try:
                self.req_get = requests.get(self.url, params=data, auth=(self.username, self.password))
                if self.req_get.status_code == 200:

                    print(enum.bs4_output(self.req_get.text))

                else:
                    print(self.colours['WARNING'] + 'Unable to make request' + self.colours['RESET'])
                    sys.exit(1)
                
            except Exception:
                
                print(self.colours['WARNING'] + 'Unable to Post!!!' + self.colours['RESET'])
                sys.exit(1)

        else:
            print(self.colours['WARNING'] + "I Don't Understand Dave" + self.colours['RESET'])