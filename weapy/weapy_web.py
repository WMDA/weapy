import requests

class Weapy:
    def __init__(self,url,*args):
        self.args=args
        self.url=url
        self.auth()
        self.host()
        print(self.req.text)
    
    def auth(self):
        if self.args:
            self.username= self.args[0]
            self.password= self.args[1]
        else:
            self.username= ()
            self.password= ()
    
    def host(self):
        self.req=requests.get(self.url,auth=(self.username,self.password))
        if self.req.status_code == 200:
           print('\nHost is responding\n')
        else:
           print(f'{self.req.status_code} recieved from host')


    def cookie_manipulator(self,cookie):
        cookies=cookie
        self.req=requests.get(self.url,auth=(self.username,self.password),cookies=cookie)

    

