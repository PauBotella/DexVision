import argparse

def cli():
    parser = argparse.ArgumentParser(
        prog='DexVision',
        description='Show pokemon animated sprites'
    )

    parser.add_argument(
        '-s', '--Shiny',
        action='store_true',
        help='Displays the pokemon in its shiny form. Only with -p flag'
    )

    parser.add_argument(
        '-p', '--pokemon',
        action='store_true',
        help='Display any Pokémon that you want'
    )
    parser.add_argument(
        '-l','--list',
        action='store_true',
        help='Displays a list of available pokemon'
    )

    parser.add_argument(
        '-n','--name',
        action='store_true',
        help='Shows the pokemon with the name'
    )

    return parser.parse_args()