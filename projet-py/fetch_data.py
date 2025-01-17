"""."""
import json
from pathlib import Path

import httpx


class FetchItem:
    """Fetch data from an API."""

    url: str = "https://api.dofusdb.fr"
    available_ids: list = 375, 2513 # Available api requests range

    def __init__(self, category: str, category_id: str) -> None:
        """Initialize FetchItem with category and category_id."""
        self.category = category
        self.category_id = category_id

    def get_paginated_items(self):  # noqa: ANN201
        """Fetch API data using httpx and return JSON response."""
        if not self.available_ids[0] < int(self.category_id) < self.available_ids[1]:
            return None
        endpoint = f"{self.url}/{self.category}/{self.category_id}"
        api_status_code: int = 200

        try:
            with httpx.Client(timeout=10) as client:
                response = client.get(endpoint)
                if response.status_code == api_status_code:
                    return response.json()  # Return JSON data as Python dict
        except httpx.RequestError:
            return None


def dl_item(item: FetchItem) -> None:
    """Download item data and save it as a JSON file."""
    output_dir = Path(f"Database/{item.category}")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / f"{item.category_id}.json"

    # Fetch the data from the API
    data = item.get_paginated_items()
    if data is None:
        return

    # Write the JSON data to the file
    with output_file.open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


# Fetch items
json_file = FetchItem("quests", "1653")
dl_item(json_file)
