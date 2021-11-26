#External modules
import sys
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
from prompt_toolkit.history import FileHistory
import os


#WeaPy Modules
from modules.prettify.colours import colors
from modules.http_requests.http_request import HTTPRequests
from weapy.arguments import clean_url, clean
import modules.prettify.enum_output as enum

def wap_arguments():

    args = [
        'set', 'options','get','reset','reset all', 'quit','techno','javascript', 'post'
        ]

    return args


class WaP:
    
    def __init__(self):
        
        self.colours = colors()
        
        print('\n')

        col = Style.from_dict({
            'name': '#00ff00 bold',
            'colon':'#0000ff'})

        message =[('class:name', 'WaP@WeaPy'),
        ('class:colon', ': ')]

        session = PromptSession(history=FileHistory('./.WaPhistory'))

        self.default_args =self.default_arguments()

        self.args = wap_arguments()

        try:
            
            while True:

                self.input = session.prompt(message, style=col)

                command = self.input.lstrip()

                self.wap_current_args()
 
                self.set_arguments()

                if command in self.args:
                    
                    self.wap_input(self.input)

                    self.wap_enum()

                else:
                    
                    self.terminal_input(self.input)
                

        except KeyboardInterrupt:
             
             print(self.colours['LIGHT_GREEN'] + '\nBYE!!' + self.colours['RESET'])
             
             sys.exit(0)

    def default_arguments(self):
        
        self.url = False
        self.password = False
        self.user = False
        self.output = False
        self.header = False
        self.verbose = False
        self.cookie = False 

    def set_arguments(self):

        try:
        
            if 'set url' in self.input:
                url = self.input.split()
                self.url = url[2]

                try: 
                    self.url = clean_url(self.url,exit_on_error=False)
                
                except Exception:
                    print(self.colours['WARNING'] + 'No known Top Level Domain specified please specify in the URL'+ self.colours['RESET'])


            if 'set password' in self.input:
                password = self.input.split()
                self.password = password[2]
           
            if 'set user' in self.input:
                user = self.input.split()
                self.user = user[2]

            if 'set header' in self.input:
                header = self.input.split()
                self.header = header[2]
                self.header = clean(self.header)


            if 'set cookie' in self.input:
                cookie = self.input.split()
                self.cookie = cookie[2]
                self.cookie = clean(self.cookie)
                        
            if 'set output' in self.input:
                
                output = self.input.split()

                if output[2].lower() =='yes' or output[2].lower() =='true':
                    self.output = True

                else:
                    print(self.colours['RED'] + self.colours['BOLD'] + "I can't Understand your input Dave do you want to show HTML output? Y/N" + self.colours['RESET'])
                    check=input()

                    if check.lower() == 'y':
                        self.output =True

            if 'set verbose' in self.input:

                verbose = self.input.split()

                if verbose[2].lower() =='yes' or verbose[2].lower() =='true':
                    self.verbose = True

                else:
                    print(self.colours['RED'] + self.colours['BOLD'] + "I can't Understand your input Dave do you want to show verbose output? Y/N" + self.colours['RESET'])
                    check=input()

                    if check.lower() == 'y':
                        self.verbose =True
                        
        except Exception:
            print(self.colours['RED']+ self.colours['BLINK'] + 'Cannot set Option. Type help for more help')

    def wap_current_args(self):

        self.arguments = {
        'url':self.url, 'password':self.password, 'user':self.user, 'output':self.output,
        'header':self.header,'verbose':self.verbose, 'cookie':self.cookie
        }

        self.help_list ={
            'url':'URL of website','password':'Password to access website, optional','user':'Username to access website, optional',
            'output': 'Prints source code to terminal screen', 'header':'set modified header. Usage is python dict ({name:value})', 
            'verbose':'prints out cookie and header information','cookie':'set cookie name and value. Usage is python dict ({name:value})'
            }


    def wap_input(self,command):

        '''
        Function to call generic WaP  commands
        '''

        if command == 'quit':
            
            print(self.colours['LIGHT_GREEN'] + '\nBYE!!' + self.colours['RESET'])
        
            sys.exit(0)

        if command == 'reset all':
                    
            self.default_arguments()


        if self.input == 'options':
                    
                self.current_output()

        if self.input == 'get':

            try: 
                self.http_request= HTTPRequests(self.arguments)

            except Exception:

                if self.url == False:
                        print(self.colours['RED'] + self.colours['BLINK'] + 'Unable to make get request, No URL sepcified!' + self.colours['RESET'])

                else:
                        print(self.colours['RED'] + self.colours['BLINK'] + 'Unable to make get request' + self.colours['RESET'])

        if self.input == 'post':
            
            try:
                self.http_request.post()

            except Exception:
                print(self.colours['RED'] + self.colours['BLINK'] + 'I cannot do that Dave, make sure you have made a GET request first' + self.colours['RESET'])


    def wap_enum(self):

        '''
        Function to call WaP enum module functions
        '''
        
        if self.input == 'techno':
            
            enum.webanalyzer_output(self.url)

    def terminal_input(self,command):

        '''
        Function so WaP can function like a normal shell.

        If command 
        '''

        if 'cd' in command:
                    
            if command != 'cd':

                cd_input= command.split()
                   
                try:
                    os.chdir(cd_input[1])

                except Exception:

                    print(self.colours['RED'] + self.colours['BOLD'] + "I can't do that Dave"  + self.colours['RESET'])
                                        
        else:
                
            try:
                os.system(command)
                    
            except Exception:
                    print(self.colours['RED'] + self.colours['BOLD'] + "I can't do that Dave"  + self.colours['RESET'] + self.colours['RESET'])

    def current_output(self):

        print('\n')
        
        print('',self.colours['PURPLE'] + self.colours['BOLD']+ '-'*200,'\n', "\t Option \t\t\t\tvalue \t\t\t\t\t\t\tHelp",'\n','-'*200,'\n' + self.colours['RESET'])
        
        for key , val in self.arguments.items():
            if len(key) <= 6:
                print('\t', str(key) + "\t\t\t\t\t" + str(val) + "\t\t\t\t\t\t\t" + self.help_list[key])
            else:
                print('\t', str(key) + "\t\t\t\t" + str(val) + "\t\t\t\t\t\t\t" + self.help_list[key])

        print('\n')

    def reset(self,input):

        if 'url' in input:
            self.url = False
        elif 'password' in input:
            self.password = False
        elif 'user' in input:
            self.user = False
        elif 'output' in input:
            self.output = False
        elif 'header' in input:
            self.header = False
        elif 'verbose' in input:
            self.verbose = False
        elif 'cookie' in input:
            self.cookie = False 
        else:
            print(self.colours['RED'] + self.colours['BOLD']+ 'I cannot understand what you are saying Dave'+ self.colours['RESET'])

