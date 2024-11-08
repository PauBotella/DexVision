from arguments import *
from cli import cli

def main():

    arguments = cli()
    try:
        #list()
        #random_pokemon()
        search_pokemon("abomasnow-mega",False)


    except Exception as ex:
        print(ex)
        exit(1)


if __name__ == '__main__':
    main()
    exit(0)