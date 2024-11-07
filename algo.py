import os
import shutil

def move_shiny_files(source_folder, destination_folder):
    # Itera sobre los archivos en la carpeta de origen
    for file_name in os.listdir(source_folder):
        source_path = os.path.join(source_folder, file_name)

        # Verifica que el elemento sea un archivo y que "Shiny" esté en el nombre
        if os.path.isfile(source_path) and "shiny" in file_name:
            destination_path = os.path.join(destination_folder, file_name)

            try:
                # Mueve el archivo
                shutil.move(source_path, destination_path)
                print(f"Movido: {file_name} -> {destination_folder}")
            except Exception as e:
                print(f"No se pudo mover el archivo {file_name}. Error: {e}")

# Ejecuta la función
move_shiny_files("Sprites", "ShinySprites")
