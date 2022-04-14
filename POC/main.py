# Écrire un programme pour lire chaque ligne d'un fichier csv donné et imprimer une liste de chaîne de caractéres 
# si location_id > 1600 alors marqués comme "chef"
# si location_id < 1600 alors marqués comme "order"
# lire dans le fichier csv department.csv et écrire dans un fichier output.txt avec la mention "chef" ou "Order" sur chaque line

#!/usr/bin/env python3

import csv

output = []

fileDepCsv = "POC/departments.csv"

with open(fileDepCsv) as fp:
    reader = csv.DictReader(fp)

    for dep in reader:
        if int(dep['location_id']) > 1600:
            line = f"Chef {dep['department_id']}, {dep['department_name']}, {dep['manager_id']}, {dep['location_id']}"
        elif int(dep['location_id']) < 1600:
            line = f"Chef {dep['department_id']}, {dep['department_name']}, {dep['manager_id']}, {dep['location_id']}"
        else:
            print("Location_id not found")
            continue

        output.append(line)

# print(output)

file_output = "POC/output.txt"

with open(file_output, "w") as fp:
    for row in output:
        fp.write(f"{row}\n")