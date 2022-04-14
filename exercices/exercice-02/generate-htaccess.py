#!/usr/bin/env python3

import csv

# Entête de notre fichier htaccess
output = [
    "Order Allow,Deny"
]

# chemin vers le fichier csv contenant les IPs
fileIpCsv = "exercices/exercice-02/ip-addresses.csv"

# condition et parcours du fichier csv
with open(fileIpCsv) as fp:
    reader = csv.DictReader(fp)
    for item in reader:

        if item['Rule'] == "Allow":
            line = f"Allow from {item['IP Address']}"
        elif item['Rule'] == "Deny":
            line = f"Deny from {item['IP Address']}"
        else:
            print(f"Rule error. Rule found : {item['Rule']}")
            continue
        
        output.append(line)

output.append("Deny from all")

print(output)

# le chemin vers le fichier htaccess.txt

file_output = "exercices/exercice-02/htaccess.txt"

with open(file_output, "w") as fp:
    for item in output:
        fp.write(f"{item}\n")