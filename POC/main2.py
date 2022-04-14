#!/usr/bin/env python3

from asyncore import write
import csv
import sys
import os
import ipaddress
import logging

from pyparsing import line

logging.basicConfig(format='%(asctime)s - [%(levelname)s] - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)

CSV_FILENAME = "exercices/exercice-04/ip-addresses.csv"
OUTPUT_FILENAME = "exercices/exercice-04/htaccess.txt"

# create function to parse file csv
def parse_csv(csv_filename=CSV_FILENAME):

    datas = [] # créer une liste vide 

    with open(csv_filename) as fp:
        reader = csv.DictReader(fp)
        for line_num, row in enumerate(reader):

            row_ip = row['IP Address']

            # ont vérifie si les adresses ip sont valident 
            try:
                ipaddress.ip_address(row_ip) 
            except Exception as err:
                msg = f"Invalid ipaddress : {row_ip} - line : {line_num}"
                logger.error(msg) # ont capture le message avec notre variable "logger" créer plus haut 
                continue 

            # condition sur les différents line de notre fichier 
            if row['Rule'] == "Allow":
                line = f"Allow from {row_ip}"
            elif row['Rule'] == "Deny":
                line = f"Deny from {row_ip}"
            else:
                logger.error(f"Unknow rule error. Rule found : row['Rule']")
                continue

            datas.append(line) # ont ajoute les différentes lines dans notre liste datas 

    return datas

# Function qui permet d'écrire dans le fichier htaccess.txt 
def write_file(datas, output_filename=OUTPUT_FILENAME):
    with open(OUTPUT_FILENAME, "w") as fp:
        for out in datas:
            fp.write(f"{out}\n")

# Function main qui appeleras les functions précédentes 
def main():

    logger.info(f"START {__file__}. Input file: {CSV_FILENAME} - Output file: {OUTPUT_FILENAME}")

    # Check if file exist in directory
    if not os.path.exists(CSV_FILENAME):
        logger.critical(f"No such file {CSV_FILENAME}")
        sys.exit(1)

    datas = parse_csv(CSV_FILENAME)

    datas.insert(0, "Order Allow,Deny")
    datas.append("Deny from all")

    write_file(datas)

    logger.info(f"END {__file__}")

if __name__ == "__main__":
    main()
