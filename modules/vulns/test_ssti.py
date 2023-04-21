import requests
from modules.enumerate.enum import bs4_parse
from bs4 import BeautifulSoup

url = 'http://10.129.227.207:8080' # This is a htb url of redpanda which has a simple ssti vuln

def ssti(url: str):
    soup = bs4_parse(url)
    forms = soup.find('form')
    inputs = soup.select("form > input")
    print(inputs)



req = requests.get(url)
ssti(req.text)
    