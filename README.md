# weapy

A command line webscrapper in python for ctfs, boot2root machines etc.

There are two ways to run weapy, a "command and control framework" similar to metasploit (work in progress) called Web analysis in python (WaP) and a command line interface way similar to cURL called weapy.

## Usage

For the weapy

~~~
python3 weapy.py [options]
~~~

For WaP

~~~
python3 WaP.py
~~~

## Weapy

~~~
usage: weapy.py [-h] [-u URL] [--user USER] [--password PASSWORD] [-o] [-j] [--css] [-s] [--comments] [-A] [-w] [-v] [--ctf] [-c COOKIE] [-H HEADER] [-X] [--xss] [--debug]

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     URL of website
  --user USER           Username to access website, optional
  --password PASSWORD   Password to access website, optional
  -o, --output          Prints source code to terminal screen
  -j, --javascript      Prints javascript source code to terminal screen
  --css                 Prints css source code to terminal screen
  -s, --search          Searches for links and directories in source code
  --comments            Searches for comments in source code
  -A, --all             Does -o, -H, -s, -w , -v --comments
  -w, --webanalyser     Analyses web technology using Wappalyzer
  -v, --verbose         prints out cookie and header information
  --ctf                 for ctfs, searches source code for comments, passwords/flags
  -c COOKIE, --cookie COOKIE
                        set cookie name and value. Usage is python dict ({name:value})
  -H HEADER, --header HEADER
                        set modified header. Usage is python dict ({name:value})
  -X, --post            Makes a post request.
  --debug               prints out args dictionary to help with development
~~~