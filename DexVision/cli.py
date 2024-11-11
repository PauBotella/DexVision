import argparse

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
        type=str,
        help='Select pokemon by name, for see the available pokemon use -l flag with grep to filter that you want'
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
args = parser.parse_args()