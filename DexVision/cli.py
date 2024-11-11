import argparse

def cli():
    parser = argparse.ArgumentParser(
        prog='DexVision',
        description='Show pokemon animated sprites'
    )

    parser.add_argument(
        '-s', '--shiny',
        action='store_true',
        help='Displays the pokemon in its shiny form. Only with -p flag'
    )

    parser.add_argument(
        '-n', '--name',
        action='store_true',
        help='Displays the name of selected pokemon. Only with -r flag'
    )

    parser.add_argument(
        '-l','--list',
        action='store_true',
        help='Displays a list of available pokemon'
    )
    parser.add_argument(
        '-r','--random',
        action='store_true',
        help="Displays a pokemon randomly"
    )
    parser.add_argument(
        'pokemon',
        nargs='?',
        help='Display any Pokémon that you want',
        default="none")
    return parser.parse_args()