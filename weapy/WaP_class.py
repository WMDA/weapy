#External modules
import sys
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
import os

#WeaPy Modules
from modules.prettify.colours import colors


def wap_arguments():
    args = ['set', 'show','set']

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

        session = PromptSession()

        self.default_args =self.default_arguments()

        try:
            
            while True:

                self.input = session.prompt(message, style=col)
                
                self.terminal_input(self.input)
                
                self.set_arguments()

                self.args()

                if 'show' in self.input:
                    
                    self.current_output()
                
        except KeyboardInterrupt:
             
             print(self.colours['LIGHT_GREEN'] + '\nBYE!!' + self.colours['RESET'])
             
             sys.exit(0)
        


    def terminal_input(self,command):
        
        args = wap_arguments()
        
        if command not in args :
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


    def default_arguments(self):
        self.url = False
        self.passwd = False
        self.user = False
        self.output = False

    def set_arguments(self):
        
        if 'set url' in self.input:
            url = self.input.split()
            self.url = url[2]

           
        if 'set password' in self.input:
            passwd = self.input.split()
            self.passwd = passwd[2]
           
        if 'set user' in self.input:
            user = self.input.split()
            self.user = user[2]
                        
        if 'set output' in self.input:
            output = self.input.split()

            if output[2].lower() =='yes':
                self.output = True
                print(self.output)

            else:
                print(self.colours['RED'] + self.colours['BOLD'] + "I can't Understand your input Dave do you want to show HTML output? Y/N" + self.colours['RESET'])
                check=input()

                if check.lower() == 'y':
                    self.output =True

    def args(self):
        self.arguments = {'URL':self.url, 'passwd':self.passwd, 'user':self.user, 'output':self.output
        }

        self.help_list =['URL of website','Password to access website, optional','Username to access website, optional' ,
                         'Prints source code to terminal screen']

    def current_output(self):
        
        print('',self.colours['PURPLE'] + self.colours['BOLD']+ '-'*100,'\n', "\t Option \t\t\tvalue",'\n','-'*100,'\n' + self.colours['RESET'])
        
        

        for key , val in self.arguments.items():
            print('\t', str(key) + "\t\t\t\t" + str(val) + "\t\t\t\t")