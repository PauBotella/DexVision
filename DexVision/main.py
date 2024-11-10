from arguments import *
from cli import cli

def main():

    args = cli()
    try:
        #Errors
        if args.pokemon != "none" and (args.list or args.random):
            print(RED+"Error: "+RESET+"Too many arguments")
            return
        elif (args.random and args.list):
            print(RED+"Error: "+RESET+"Too many arguments")
            return
        elif args.pokemon == "none" and not (args.list or args.random):
            print(RED+"Error: "+RESET+"Add a pokemon or use -h to see the help")

        #actions
        if args.pokemon != "none":
            search_pokemon(args.pokemon,args.shiny)
        elif args.random:
            random_pokemon(args.name)
        elif args.list:
            list_pokemon()

    except Exception as ex:
        print(ex)

if __name__ == '__main__':
    main()