import os
import random
import json

directory = "/home/joel/.config/qtile/images/"
files = [directory+f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
print(files)

indexado = {str(i+1): file for i, file in enumerate(files)}

with open('wallpapers.json', 'w') as archivo_json:
    json.dump(indexado, archivo_json, indent=4)
