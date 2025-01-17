import json  # noqa: D100
from pathlib import Path

import httpx


class FetchItem:
  """."""

  url:str = "https://api.dofusdb.fr"

  def __init__(self, category:str, category_id:str) -> None:
    """."""
    self.category = category
    self.category_id = category_id

    self.available_ids:list = [375, 2513]

  def get_paginated_items(self):  # noqa: ANN201
    """Fetch API data using httpx and return JSON response."""
    if not self.available_ids[0] < self.category_id < self.available_ids[1]:
      return
    endpoint = f"{self.url}/{self.category}/{self.category_id}"
    api_status_code: int = 200

    try:
      # Use httpx to send a GET request
      with httpx.Client(timeout=10) as client:
        response = client.get(endpoint)
        if response.status_code == api_status_code:
          return response.json()
    except httpx.RequestError:
      return None
  
  def dl_item(self, item):
    """."""
    output_dir = Path(f"Database/{self.category}")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / f"{self.category_id}.json"
    with output_file.open("w", encoding="utf-8") as file:
      json.dump(item, file, ensure_ascii=False, indent=4)

# Fetch items
json_file = FetchItem("quests", "1653").get_paginated_items()
