from arguments import *
from cli import cli

def main():

    arguments = cli()
    try:
        #list()
        randomPoke()


    except Exception as ex:
        print(ex)
        exit(1)


if __name__ == '__main__':
    main()
    exit(0)