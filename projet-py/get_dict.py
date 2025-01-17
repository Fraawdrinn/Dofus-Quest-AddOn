import json
from pathlib import Path

from fetch_data import FetchItem

i: int = 375

while i != 2513:
    i += 1
    data: FetchItem = FetchItem("quests", str(i)).get_paginated_items()
    if data:
        db_path = Path("Database/other/negro.json")
        db_path.parent.mkdir(parents=True, exist_ok=True)  # Ensure the directory exists

        # Load existing database or initialize an empty dictionary
        if db_path.exists():
            with db_path.open("r", encoding="utf-8") as db_file:
                try:
                    db = json.load(db_file)  # Load existing JSON as a dictionary
                except json.JSONDecodeError:
                    db = {}  # File is empty or invalid JSON
        else:
            db = {}

        # Add the new entry to the dictionary
        name: str = data["name"]["en"]
        value: int = data["id"]
        db[name] = value

        # Write the updated dictionary back to the file
        with db_path.open("w", encoding="utf-8") as db_file:
            json.dump(db, db_file, ensure_ascii=False, indent=4)
    else:
        print(f"Error fetching data for ID: {i}")
