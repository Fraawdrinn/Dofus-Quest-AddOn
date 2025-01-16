import json  # noqa: D100
from pathlib import Path

import httpx

BASE_URL = "https://api.dofusdb.fr"
category: str = "quests"
category_id: str = "1653"

def get_paginated_items():  # noqa: ANN201
    """Fetch API data using httpx and return JSON response."""
    endpoint = f"{BASE_URL}/{category}/{category_id}"
    api_status_code: int = 200

    try:
        # Use httpx to send a GET request
        with httpx.Client(timeout=10) as client:
            response = client.get(endpoint)
            if response.status_code == api_status_code:
                return response.json()
    except httpx.RequestError:
        return None

# Fetch items
items = get_paginated_items()

# Save the data to a JSON file if items exist
if items:
    output_dir = Path(f"Database/{category}")
    # output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / f"{category_id}.json"
    with output_file.open("w", encoding="utf-8") as file:
        json.dump(items, file, ensure_ascii=False, indent=4)
