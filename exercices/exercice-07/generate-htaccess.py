#!/usr/bin/env python3

import csv
import sys
import os
import ipaddress
import logging
import argparse

logger = logging.getLogger(__name__)

CSV_FILENAME = "ip-addresses.csv"
OUTPUT_FILENAME = os.environ.get("LBN_OUTPUT_FILENAME", "htaccess.txt")


def parse_csv(csv_filename=CSV_FILENAME):
    """Parse CSV File
    
    :param csv_filename: CSV File Name
    :type csv_filename: str
    :return: A Array of IP Address with Allow/Deny rule
    :rtype: list
    """

    datas = []

    with open(csv_filename) as fp:
        # Parse file to dict
        reader = csv.DictReader(fp)
        
        for line_num, row in enumerate(reader):

            row_ip = row['IP Address']

            logger.debug("row : %s" % row_ip)
            
            try:
                # Check if valid ip address
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
                # exclude invalid rule and log
                logger.error(f"Unknow rule error. Rule found : row['Rule']")
                continue
            
            datas.append(line)

    return datas


def write_file(datas, output_filename=OUTPUT_FILENAME):
    """Write htaccess file on disk
    
    :param datas: Array of IPAddress and rules
    :type datas: list
    :param output_filename: htaccess filepath (default: htaccess.txt)
    :type output_filename: str
    """

    with open(OUTPUT_FILENAME, "w") as fp:
        for out in datas:
            fp.write(f"{out}\n")

def options():
    
    parser = argparse.ArgumentParser(
        description='Htaccess Generator',
        formatter_class=argparse.RawTextHelpFormatter,
        add_help=True,
    )

    parser.add_argument(
        '--csv-filepath', '-C',
        dest='csv_filepath',
        help='CSV Filepath. Default: %(default)s',
        default=CSV_FILENAME,
    )

    parser.add_argument(
        '--output-filepath', '-O',
        dest='output_filepath',
        help='Output Filepath. Default: %(default)s',
        default=OUTPUT_FILENAME,
    )

    parser.add_argument('--debug', '-D', action="store_true")

    return parser.parse_args()

def main():
    """main function"""

    args = options()

    logging_level = logging.INFO

    if args.debug:
        logging_level = logging.DEBUG

    logging.basicConfig(format='%(asctime)s - [%(levelname)s] - %(message)s', level=logging_level)

    logger.info(f"START {__file__}. Input file: {CSV_FILENAME} - Output file: {OUTPUT_FILENAME}")

    if not os.path.exists(args.csv_filepath):
        logger.critical(f"No such file : {args.csv_filepath}")
        sys.exit(1)
    
    # Parse CSV file
    datas = parse_csv(args.csv_filepath)
    
    # Add requires informations to first and last line
    datas.insert(0, "Order Allow,Deny")
    datas.append("Deny from all")
    
    write_file(datas, output_filename=args.output_filepath)

    logger.info(f"END {__file__}")

if __name__ == "__main__":
    main()
