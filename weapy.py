#External Modules
import sys

#WeaPy Modules
from weapy.arguments import arguments
from modules.prettify.colours import colors
from weapy.weapy_class import WeaPy

if __name__ == '__main__':
    
    arg = arguments()
    
    try:
        WeaPy(arg)

    except KeyboardInterrupt:
        
        colours = colors()
        print(colours['WARNING'] + '\nUser initiated shutdown' + colours['RESET'])
        print(colours['BLUE'] + '\nBYE!!' + colours['RESET'])
        sys.exit(0)
