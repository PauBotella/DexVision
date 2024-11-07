import random
import os

path="../Sprites/"


pokes = [f for f in os.listdir(path)]

def list():
    for sprite in pokes:
        print(os.path.splitext(sprite)[0])

def randomPoke():
    
    random_number = random.randrange(100)
    random_poke_list = []
    #depending on the random number, a shiny pokemon will be appear or not. 5% chance of shiny
    if random_number <= 5:
        random_poke_list = [f for f in os.listdir(path) if "shiny" in f]
    else:
        random_poke_list = [f for f in os.listdir(path) if "shiny" not in f]

    random_poke = random.choice(random_poke_list)
    print(random_poke)
    print(random_number)
    random_poke_path = os.path.join(path, random_poke)
    os.system("kitty +kitten icat --align left "+random_poke_path)
    

def check_exists(sprite):
    return os.path.isfile(path+sprite+".gif")