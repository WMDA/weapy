import requests
import sys
from colorama import *

class Weapy:
    def __init__(self,url,output,username,password):

        self.url=url
        self.password=password
        self.username=username
        self.host(output)
    
    def host(self,output):
        
        try:
            self.req=requests.get(self.url,auth=(self.username,self.password))
        
        except Exception:
            print(Fore.RED + '\nCONNECTIVITY ERROR\n',Fore.WHITE +'\nUnable to connect to host.\nIs this a valid website?\nCheck your connectivity\n')
            
            sys.exit(1)
        
        if self.req.status_code == 200:

            print(Fore.MAGENTA + '\nHost is responding\n')    
            
            if output==True:
                print(self.req.text)
        else:
            print(Fore.RED + f'{self.req.status_code} recieved from host')

       
    def cookie_manipulator(self,cookie):
        cookies=cookie
        self.req=requests.get(self.url,auth=(self.username,self.password),cookies=cookie)


    

