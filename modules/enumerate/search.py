import re

#Weapy modules
from modules.prettify.colours import colors
from modules.enumerate.enum import bs4_parse

def text(website_code:str, search_parameter:str) -> None:

    '''
    Function to search page source code for spefic text.

    Parameters
    ---------
    website_code:str Source code from website
    search_parameter:str Text to search for

    Returns
    -------
    prints to console if text has been found
    '''

    colours = colors()
    search = re.findall(rf'.*{search_parameter}.*', website_code)

    if len(search) > 0:
        beautify = [re.sub(rf'{search_parameter}', colours['GREEN'] + colours['BOLD'] + search_parameter + colours['RESET'], text ) for text in search]
        print(colours['CYAN'] + f'\nFound {search_parameter} on the page' + colours['RESET'])
        print('\n', *beautify, '\n', sep='\n')

    else:
        print(colours['RED'] + f'\nCould not find {search_parameter} on the page' + colours['RESET'], '\n')

def dirs_search(text) -> None:

    remove_ending_tags = re.sub(r'</.*?>', '', text)
    remove_html_links = re.sub(r'(http.*//.*?[^\'"><]+)','', remove_ending_tags)
    dir_list = re.findall(r'/[A-Za-z0-9_\.]*', remove_html_links)
    
    
    further_search = re.findall(r'.*?/.*?', remove_html_links)
    further_search_results = [re.sub(r'<.*?=','', dir) for dir in further_search]
    
    common_dirs = ['files','uploads', 'images']
    strip = [dirs.lstrip('/"').rstrip('/') for dirs in further_search_results]
    remove_tabs = [dirs.lstrip('\t"').rstrip('\t') for dirs in strip ]
    results = [dirs for dirs in remove_tabs if dirs in common_dirs]

    filter_no_dir = [dir for dir in dir_list if len(dir) > 1]
    filter_links = [dir for dir in filter_no_dir if '.' not in dir]
    dirs = filter_links + results
    dirs = list(set(dirs))

    return dirs



def file_search(text):
    
    file_type = ['gif', 'txt', 'jpeg', 'html', 'py', 'png', 'php']
    files = []
    
    for format in file_type:     
        file_list = re.findall(r'[A-Za-z0-9-_]*.{}'.format(format), text)
        
        for file in file_list:
            if file not in files:
                if '.'in file:
                    files.append(file)

    return files