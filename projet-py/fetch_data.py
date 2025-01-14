import json

import requests

BASE_URL = "https://api.dofusdb.fr"
object:str = "quests"
id:str = "1653"


def get_paginated_items():
    endpoint = f"{BASE_URL}/{object}/{id}"
    api_status_code: int = 200

    try:
        response = requests.get(endpoint,) #httpx
        if response.status_code == api_status_code:
            return response.json()
        else:
            # Response error
            print(f"Error: Received status code {response.status_code}")
            print(response.text)
        #  URL error
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# Fetch items
items = get_paginated_items(page=1, limit=500)

# Save the data to a JSON file
if items:
    with open(f"outputs/{object}/{object}_{id}.json", "w", encoding="utf-8") as file:
        json.dump(items, file, ensure_ascii=False, indent=4)  # Pretty print with indent
    print(f"Data saved to {object}_{id}.json")
else:
    print("No data to save.")

