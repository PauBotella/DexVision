import random
import os

path="../Sprites/"
command="kitty +kitten icat --align left "
pokes = [f for f in os.listdir(path) if "shiny" not in f]
shiny_pokes = [f for f in os.listdir(path) if "shiny" in f]

def list():
    for sprite in pokes:
        print(os.path.splitext(sprite)[0])

def random_pokemon():
    random_number = random.randrange(100)
    random_poke_list = path if random_number <= 5 else shiny_pokes

    random_poke = random.choice(random_poke_list)
    random_poke_path = os.path.join(path, random_poke)
    os.system(command+random_poke_path)

def search_pokemon(sprite,is_shiny):
    
    complete_path = path+sprite+".gif" if not is_shiny else path+sprite+"_shiny.gif"

    if not os.path.isfile(complete_path):
        print("Pokemon not found, try -l to search the pokemon that you want")
        return
    os.system(command+complete_path)
