import json

data = 0

with open("projet/outputs/quests/quests_1653.json") as questFile :
    data = json.load(questFile)

print(data["steps"][0]["objectives"][0]["map"]["posX"])