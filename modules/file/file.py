import re
from weapy.weapy_class import WeaPy

def directories(filename):
    dirs = []
    with open(filename) as f:
        content = f.read().splitlines()
        for line in content:
            file = re.findall(r'^.*?\s', line)
            dirs.append(file)
    return dirs

def get_url(filename, url):
    urls= []
    dir = directories(filename)
    for directory in dir:
        urls.append(url + directory[0])

    return urls

def file_modules(args):
    url = args['url']
    filename = args['file']
    urls = get_url(filename, url) 
    for ip in urls:
        args.update({'url':ip})
        WeaPy(args)
        





