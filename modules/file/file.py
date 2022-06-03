import re


def directories(filename):
    dirs = []
    with open(filename) as f:
        content = f.read().splitlines()
        for line in content:
            file = re.findall(r'^/.*?\W', line)
            dirs.append(file)
    return dirs

def url(filename, url):
    dir = directories(filename)
    for directory in dir:
        print(url + directory[0])