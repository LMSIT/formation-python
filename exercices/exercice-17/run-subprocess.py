#!/usr/bin/env python3

import os
import sys
import argparse
import subprocess

def list_dir(path):
    cmd = f"ls -l {path}"
    result = subprocess.run(cmd, shell=True, check=True, capture_output=True)
    #print("SUCCESS : ", result.returncode == 0)
    print(result.stdout.decode())

def options():
    
    parser = argparse.ArgumentParser(
        description="list directory",
        formatter_class=argparse.RawTextHelpFormatter,
        add_help=True,
    )

    parser.add_argument(
        "--path",
        "-p",
        dest="path",
        help="Path listing. Default: %(default)s",
        default='/tmp',
    )

    return parser.parse_args()


def main():
    """main function"""

    args = options()

    if not os.path.exists(args.path):
        sys.stderr.write(f"No such file : {args.path}\n")
        sys.exit(1)

    list_dir(args.path)

if __name__ == "__main__":
    main()
