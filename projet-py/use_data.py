import json

def find_all_pos_coordinates(data):
    results = []
    if isinstance(data, dict):
        for key, value in data.items():
            if key == "map" and isinstance(value, dict) and "posX" in value and "posY" in value:
                results.append((value["posX"], value["posY"]))
            else:
                results.extend(find_all_pos_coordinates(value))
    elif isinstance(data, list):
        for item in data:
            results.extend(find_all_pos_coordinates(item))
    return results

# Read the JSON file with UTF-8 encoding
with open("projet-py/outputs/quests/quests_1653.json", 'r', encoding='utf-8') as questFile:
    data = json.load(questFile)

# Find all posX and posY values
all_pos_coordinates = find_all_pos_coordinates(data)

# Group coordinates by their values
grouped_coordinates = {}
for coord in all_pos_coordinates:
    if coord not in grouped_coordinates:
        grouped_coordinates[coord] = []
    grouped_coordinates[coord].append(coord)

# Convert to list of lists
coordinate_lists = list(grouped_coordinates.values())


# Remove duplicates while maintaining order
seen = set()
unique_coordinates = []
for coord in all_pos_coordinates:
    if coord not in seen:
        unique_coordinates.append(coord)
        seen.add(coord)

# Convert the unique coordinates to a list of lists
coordinates_list_of_lists = [[x, y] for x, y in unique_coordinates]

# Print the list of lists
print("Coordinates as a list of lists:")
print(coordinates_list_of_lists)
