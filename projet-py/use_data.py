import json
from pathlib import Path


class Data:
    """"""
    def __init__(self, file_path: str):
        """"""
        self.file_path = Path(file_path)
        self.data = self._load_data()

    def _load_data(self) -> json:
        """"""
        # Load JSON data from the file.
        with self.file_path.open(encoding="utf-8") as quest_file:
            return json.load(quest_file)

    def find_all_pos_coordinates(self, data: None=None) -> list:
        """Recursively find all posX and posY coordinates in the data."""
        if data is None:
            data = self.data

        results = []
        stack = [data]  # Avoid recursion depth issues(chatGPT)

        while stack:
            current = stack.pop()

            if isinstance(current, dict):
                for key, value in current.items():
                    if key == "map" and isinstance(value, dict) and "posX" in value and "posY" in value:
                        results.append((value["posX"], value["posY"]))
                    else:
                        stack.append(value)
            elif isinstance(current, list):
                stack.extend(current)

        return results

    def get_unique_coordinates(self) -> list:
        """Extract unique posX and posY coordinates as a list of lists."""
        all_pos_coordinates = self.find_all_pos_coordinates()

        # Remove duplicates while maintaining order
        seen = set()
        unique_coordinates = []
        for coord in all_pos_coordinates:
            if coord not in seen:
                unique_coordinates.append(coord)
                seen.add(coord)

        return [[x, y] for x, y in unique_coordinates]

    def get_grouped_coordinates(self) -> list:
        """Group coordinates by their values."""
        all_pos_coordinates = self.find_all_pos_coordinates()

        grouped_coordinates = {}
        for coord in all_pos_coordinates:
            if coord not in grouped_coordinates:
                grouped_coordinates[coord] = []
            grouped_coordinates[coord].append(coord)

        return list(grouped_coordinates.values())

file_path = "projet-py/outputs/quests/quests_1653.json"
extractor = Data(file_path)

#unique coordinates
unique_coordinates = extractor.get_unique_coordinates()

def main():
    """"""
    print("Unique coordinates as a list of lists:")
    print(unique_coordinates)

    #grouped coordinates
    grouped_coordinates = extractor.get_grouped_coordinates()
    print("Grouped coordinates:")
    print(grouped_coordinates)

if __name__ == "__main__":
    main()
