#!/usr/bin/env python3

import csv
import sys
import os
import ipaddress
import logging

logging.basicConfig(format='%(asctime)s - [%(levelname)s] - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)

CSV_FILENAME = "ip-addresses.csv"
OUTPUT_FILENAME = "htaccess.txt"


def parse_csv(csv_filename=CSV_FILENAME):

    datas = []

    with open(csv_filename) as fp:
        reader = csv.DictReader(fp)
        for line_num, row in enumerate(reader):

            row_ip = row['IP Address']
            
            try:
                ipaddress.ip_address(row_ip)
            except Exception as err:
                msg = f"Invalid ipaddress : {row_ip} - line : {line_num}"
                logger.error(msg)
                continue
            
            if row['Rule'] == "Allow":
                line = f"Allow from {row_ip}"
            elif row['Rule'] == "Deny":
                line = f"Deny from {row_ip}"
            else:
                logger.error(f"Unknow rule error. Rule found : row['Rule']")
                continue
            
            datas.append(line)

    return datas


def write_file(datas, output_filename=OUTPUT_FILENAME):
    with open(OUTPUT_FILENAME, "w") as fp:
        for out in datas:
            fp.write(f"{out}\n")


def main():

    logger.info(f"START {__file__}. Input file: {CSV_FILENAME} - Output file: {OUTPUT_FILENAME}")

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
