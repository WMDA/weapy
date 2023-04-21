import requests
from modules.enumerate.enum import bs4_parse, get_form_details, find_input_forms
from bs4 import BeautifulSoup

url = 'http://10.129.227.207:8080' # This is a htb url of redpanda which has a simple ssti vuln


def ssti(url: str):
    soup = bs4_parse(url)
    f = find_input_forms(url)
    l = get_form_details(f)
    data = l['inputs'][0]['value'].update('hello')

    print(data)

    #vulnerable_request = requests.post(url, data={})

    
req = requests.get(url)
print(req)
ssti(req.text)
    