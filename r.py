import os
import json

directorio = 'D:/Me/Projects/juacar/img/juacar-2024'  # Reemplaza con la ruta de tu directorio
archivo_json = 'nombres_archivos.json'  # Nombre del archivo JSON

# Obtén la lista de archivos en el directorio
archivos = os.listdir(directorio)

# Ordena la lista de archivos
archivos.sort()

# Crea una lista con los nombres de los archivos
nombres_archivos = [ " {src: " + f"'./img/juacar-2024/{archivo}'" + ", text: 'Prueba millll'}" for archivo in archivos]

# Crea un diccionario con el formato deseado
data = {"archivos": nombres_archivos}

# Escribe el diccionario en un archivo JSON
with open(archivo_json, 'w') as json_file:
    json.dump(data, json_file, indent=2)

print(f'Nombres de archivos guardados en {archivo_json} con éxito.')
