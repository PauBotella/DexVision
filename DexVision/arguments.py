import random
import os

RED = '\033[91m'
RESET = "\033[0m"
path="../Sprites/"
command="kitty +kitten icat --align left "
pokes = [f for f in os.listdir(path) if "shiny" not in f]
shiny_pokes = [f for f in os.listdir(path) if "shiny" in f]

def list_pokemon():
    for sprite in pokes:
        print(os.path.splitext(sprite)[0])

def random_pokemon(name):
    random_number = random.randrange(100)
    random_poke_list = shiny_pokes if random_number <= 5 else pokes
    random_poke = random.choice(random_poke_list)
    random_poke_path = os.path.join(path, random_poke)
    if name:
        print(os.path.splitext(random_poke)[0])
    os.system(command+random_poke_path)

def search_pokemon(sprite,is_shiny):
    complete_path = path+sprite+".gif" if not is_shiny else path+sprite+"_shiny.gif"

    if not os.path.isfile(complete_path):
        print(RED+"Error: "+RESET+"Pokemon not found, try -l to search the pokemon that you want")
        return
    os.system(command+complete_path)
