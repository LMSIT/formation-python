#!/usr/bin/env python3

import csv

output = [
    "Order Allow,Deny"
]

import logging

logging.basicConfig(filename='/tmp/example.log', level=logging.INFO)

logger = logging.getLogger(__name__)


with open('ip-addresses.csv') as fp:
    reader = csv.DictReader(fp)
    for row in reader:
        
        if row['Rule'] == "Allow":
            line = f"Allow from {row['IP Address']}"
        elif row['Rule'] == "Deny":
            line = f"Deny from {row['IP Address']}"
        else:
            print(f"Rule error. Rule found : row['Rule']")
            continue
        
        output.append(line)

output.append("Deny from all")

with open("htaccess.txt", "w") as fp:
    for out in output:
        fp.write(f"{out}\n")
