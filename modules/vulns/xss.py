from modules.enumerate.enum import input_forms
from modules.http_requests.http_request import HTTPRequests


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



