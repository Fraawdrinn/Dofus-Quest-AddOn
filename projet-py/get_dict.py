import json
from pathlib import Path

# Ouvrir et charger le fichier JSON
with Path("Database/all.json").open(encoding="utf-8") as db:
    data = json.load(db)  # Charger le contenu du fichier JSON dans un dictionnaire

# Imprimer toutes les clés d'un coup
steps = data["data"][0]["steps"]

for el in steps:
  print(el["id"])
