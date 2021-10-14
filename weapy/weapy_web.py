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

            print(Fore.GREEN + '\nHost is responding\n' + Fore.WHITE)    
            
            if output==True:
                print(self.bs4_output(self.req.text))

        else:
            print(Fore.RED + f'{self.req.status_code} recieved from host')

    def bs4_output(self,text):
        
        from bs4 import BeautifulSoup
        import re
        
        '''
        Removes the <br> tag cand changes it to a standard space
        Also removes all the odd output to standard html tags
        '''
        line_break= re.sub(r'<br />','\n',text)
        tag_left= re.sub(r'&lt;','<',line_break)
        tag_right= re.sub(r'&gt;','>',tag_left)
        output= re.sub(r'&nbsp;',' ',tag_right)
        soup = BeautifulSoup(output, features="lxml")
        pretty= soup.prettify()
        
        '''
        Finds all the tags and changes what is inside the tags to purple 
        and the rest white.
        '''
        color_beg= re.sub(r'<', Fore.MAGENTA + ' <',pretty)
        final_output= re.sub(r'>', '> '+ Fore.WHITE, color_beg)
        
        return(final_output)

    def cookie_manipulator(self,cookie):
        cookies=cookie
        self.req=requests.get(self.url,auth=(self.username,self.password),cookies=cookie)


    

