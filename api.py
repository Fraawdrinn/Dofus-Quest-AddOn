# By Fraawdrinn
# This program helps fetching data from to json (here for Dofus)

import tkinter as tk
import requests

def search_item():
    item_name = entry.get()
    url = f"https://dofusdb.fr/api/database/quest/{item_name}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        result_label.config(text=data[0]["name"] + " - Niveau : " + str(data[0]["level"]))
    else:
        result_label.config(text="quête non trouvé.")

# Interface Tkinter
window = tk.Tk()
window.title("Recherche DofusDB")

tk.Label(window, text="Nom de la quête :").pack()
entry = tk.Entry(window)
entry.pack()

tk.Button(window, text="Rechercher", command=search_item).pack()
result_label = tk.Label(window, text="")
result_label.pack()

def main():
    window.mainloop()
    return

if __name__ == '__main__':
    main()



# import requests

# # Endpoint pour rechercher un objet par nom
# url = "https://api.dofusdb.fr"

# # Paramètres de recherche
# params = {
#     "search": "Bouclier Feudala"  # Nom de l'objet à chercher
# }

# # Requête GET
# response = requests.get(url, params=params)

# # Vérifier le statut de la réponse
# if response.status_code == 200:
#     data = response.json()  # Convertir la réponse en JSON
#     print(data)
# else:
#     print(f"Erreur : {response.status_code}")
