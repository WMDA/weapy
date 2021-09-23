from args import arguments
from weapy_web import Weapy

if __name__ == '__main__':
    arg=arguments()
    
    if not arg.user:
        arg.user=()
    
    if not arg.password:
        arg.password=()
    
    if not arg.output:
        arg.output=False

    Weapy(arg.url,arg.output,arg.user,arg.password)
