import os
import random

def randomPoke(folder):

    if not os.path.isdir(folder):
        print("La carpeta especificada no existe.")
        return
    
    archivos = [f for f in os.listdir(folder)]
    
    if not archivos:
        print("No hay archivos en la carpeta especificada.")
        return
    
    archivo_seleccionado = random.choice(archivos)    
    ruta_archivo=os.path.join(folder, archivo_seleccionado)
    os.system("kitty +kitten icat --align left "+ruta_archivo)

# Especifica la carpeta
folder = "/home/pau/Documents/AnimatedSprites"  # Cambia esto a la ruta de tu carpeta
randomPoke(folder)
