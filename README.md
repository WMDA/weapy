# weapy

Weapy is a source code reader primarly aimed at bug bounty/CTF competitions.

weapy will parse through source code for specific text, forms, flags (for ctf competitions), passwords, comments as well as giving some information on the back end technology of the website.

EXPERIMENTAL
WaP is a cmd prompt for weapy which is work in progress.

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
usage: weapy.py [-h] [-u URL] [--user USER] [--password PASSWORD] [-o] [-j] [--css] [-s] [--comments] [-A] [-w] [-v] [--ctf] [-c COOKIE] [-H HEADER] [-X] [--debug] [-t TEXT] [-f]

options:
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
  -t TEXT, --text TEXT  Searches website code for specific text
  -f, --forms           Finds forms on the page
~~~
