from modules.enumerate.enum import input_forms
from modules.http_requests.http_request import HTTPRequests
from modules.utils.utils import load_json
import os 


def payloads():
    payloads={
        'basic': "<script>alert('weapy');</script>"
        }

    return payloads


def xss_scanner(args,request):
    pload = payloads() 
    post = HTTPRequests()
    post.post()
    
    for key,val in pload.items():
        forms = input_forms(request,val,vulns=True)


def lfi(url):
    data = load_json()
    print(data)
    #with open(os.path.join(os.getcwd(), data['wordlist_location'], data['subdomain_wordlist']) as word:
    #    word = word.rstrip('\n')
