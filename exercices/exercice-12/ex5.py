import json

with open("file.json") as fp:
    data = json.load(fp)

print(data)