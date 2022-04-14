#!/usr/bin/env python3

from asyncio.log import logger
import csv
import sys
import os
import ipaddress
import logging

logging.basicConfig(
    filename='exercices/exercice-03/example.log', 
    format='%(asctime)s - [%(levelname)s] - %(message)s', 
    level=logging.INFO
)

logger = logging.getLogger(__name__)

# Ici c'est l'entête de notre fichier htaccess 
output = [
    "Order Allow,Deny"
]

# le chemin relative vers notre fichier htaccess
CSV_FILENAME = "exercices/exercice-03/ip-addresses.csv"
OUTPUT_FILENAME = "exercices/exercice-03/htaccess.txt"

# Check if csv_filename exist
if not os.path.exists(CSV_FILENAME):
    logger.critical(f"No such file {CSV_FILENAME}")
    sys.exit(1)

logger.info(f"START {__file__}. Input file: {CSV_FILENAME} - Output file: {OUTPUT_FILENAME}")

with open(CSV_FILENAME) as fp:
    reader = csv.DictReader(fp)
    for line_num, row in enumerate(reader):

        row_ip = row['IP Address']

        try:
            ipaddress.ip_address(row_ip)
        except Exception as err:
            msg = f"Invalid ipaddress : {row_ip} - line : {line_num}"
            logger.error(msg)
            continue

        if row ['Rule'] == "Allow":
            line = f"Allow from {row_ip}"
        elif row['Rule'] == "Deny":
            line = f"Deny from {row_ip}"
        else:
            logger.error(f"Unknow rule error. Rule found : row['Rule']")
            continue

        output.append(line)

output.append("Deny from all")

with open(OUTPUT_FILENAME, "w") as fp:
    for out in output:
        fp.write(f"{out}\n")

logger.info(f"END {__file__}")
