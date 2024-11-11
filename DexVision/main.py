from arguments import *
from cli import *

def main():
    try:
        #Errors
        if args.name and (args.list or args.random):
            print(RED+"Error: "+RESET+"Too many arguments")
            return
        elif (args.random and args.list):
            print(RED+"Error: "+RESET+"Too many arguments")
            return

        #actions
        if args.name:
            search_pokemon(args.name,args.shiny)
        elif args.random:
            random_pokemon()
        elif args.list:
            list_pokemon()
        else:
            parser.print_help()
    except Exception as ex:
        print(ex)

if __name__ == '__main__':
    main()