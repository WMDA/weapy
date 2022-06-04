#External Modules
import sys

#WeaPy Modules
from weapy.arguments import arguments
from modules.prettify.colours import colors
from weapy.weapy_class import WeaPy
from modules.file.file import file_modules  

if __name__ == "__main__":
    
    arg = arguments()
    
    if arg['file'] != False:

        try:
            file_modules(arg)
        
        except KeyboardInterrupt:
        
            colours = colors()
            print(colours['WARNING'] + '\nUser initiated shutdown' + colours['RESET'])
            print(colours['BLUE'] + '\nBYE!!' + colours['RESET'])
            sys.exit(0)

    else:

        try:
            WeaPy(arg)

        except KeyboardInterrupt:
        
            colours = colors()
            print(colours['WARNING'] + '\nUser initiated shutdown' + colours['RESET'])
            print(colours['BLUE'] + '\nBYE!!' + colours['RESET'])
            sys.exit(0)
