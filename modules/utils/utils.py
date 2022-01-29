import requests
import json
import os


def load_json():
    os.chdir('../../wordlist')
    with open('config.json') as f:
        data = json.load(f)

    return data
