import json
import os
import random
# Ruta al archivo JSON
ruta_json = os.path.join(os.path.dirname(__file__), 'wallpapers.json')

#Cargar el contenido del archivo JSON
with open(ruta_json, 'r') as archivo_json:
    indexado_archivos = json.load(archivo_json)

wallpapers = list(indexado_archivos.values())

