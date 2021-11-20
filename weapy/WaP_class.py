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


def wap_arguments():
    args = ['set', 'options','get','reset']

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

        try:
            
            while True:

                self.input = session.prompt(message, style=col)
                
                self.terminal_input(self.input)
                
                self.set_arguments()

                self.args()

                if self.input == 'options':
                    
                    self.current_output()

                if self.input == 'reset':
                    self.default_arguments()


                if self.input == 'get':

                     self.http_request= HTTPRequests(self.arguments)
                    
                
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
                self.url = clean_url(self.url)

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

                        
            if 'set output' in self.input:
                output = self.input.split()

                if output[2].lower() =='yes' or output[2].lower() =='true':
                    self.output = True

                else:
                    print(self.colours['RED'] + self.colours['BOLD'] + "I can't Understand your input Dave do you want to show HTML output? Y/N" + self.colours['RESET'])
                    check=input()

                    if check.lower() == 'y':
                        self.output =True
                        
        except Exception:
            print(self.colours['RED']+ self.colours['BLINK'] + 'Cannot set Option. Type help for more help')

    def args(self):

        self.arguments = {
        'url':self.url, 'password':self.password, 'user':self.user, 'output':self.output,
        'header':self.header,'verbose':self.verbose, 'cookie':self.cookie
        }

        self.help_list ={
            'url':'URL of website','password':'Password to access website, optional','user':'Username to access website, optional',
            'output': 'Prints source code to terminal screen', 'header':'set modified header. Usage is python dict ({name:value})', 
            'verbose':'prints out cookie and header information','cookie':'set cookie name and value. Usage is python dict ({name:value})'
            }


    def terminal_input(self,command):
        
        args = wap_arguments()
        
        command = command.lstrip()

        if command not in args :

                if 'cd' in command:
                    
                    if command != 'cd':
                        cd_input= command.split()
                   
                    try:
                        os.chdir(cd_input[1])

                    except Exception:
                        print(self.colours['RED'] + self.colours['BOLD'] + "I can't do that Dave"  + self.colours['RESET'])

                elif command == 'quit':
                    print(self.colours['LIGHT_GREEN'] + '\nBYE!!' + self.colours['RESET'])
                    sys.exit(0)
                    
                    
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