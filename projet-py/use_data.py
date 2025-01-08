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
print("All (posX, posY) coordinates found:")
for coordinates in all_pos_coordinates:
    print(coordinates)

# Group coordinates by their values
grouped_coordinates = {}
for coord in all_pos_coordinates:
    if coord not in grouped_coordinates:
        grouped_coordinates[coord] = []
    grouped_coordinates[coord].append(coord)

# Convert to list of lists
coordinate_lists = list(grouped_coordinates.values())

print("\nGrouped coordinates:")
for coord_list in coordinate_lists:
    print(coord_list)

# Write the data back to a new JSON file with UTF-8 encoding
with open('projet-py/outputs/other/output_utf8.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("\nThe UTF-8 encoded JSON has been written to 'projet-py/outputs/other/output_utf8.json'")
