import requests
import json
import os


def load_json():
    with open('config.json') as f:
        data = json.load(f)

    return data

data =load_json()



sub_list = open(os.path.join(os.getcwd(), data['wordlist_location'], data['subdomain_wordlist'])).read()