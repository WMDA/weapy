from standalone import arguments
from weapy_class import WeaPy
from utils import colors
import sys

if __name__ == '__main__':
    
    arg = arguments()
    
    try:
        WeaPy(arg)

    except KeyboardInterrupt:
        
        colours = colors()
        
        print(colours['WARNING'] + '\nUser initiated shutdown' + colours['RESET'])
        
        print(colours['BLUE'] + '\nBYE!!' + colours['RESET'])
        
        sys.exit(0)
