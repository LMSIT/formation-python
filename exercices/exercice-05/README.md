# Htaccess file generator

This tool is used to generate an [.htaccess](http://httpd.apache.org/docs/current/howto/htaccess.html) file for Apache from a CSV file containing IP addresses and rules.

## Requirements

- Python 3.5+

## Installation

- No installation require

## CSV File Format

```csv
IP Address,Rule
192.168.1.10,Allow
172.100.2.11,Allow
2.2.2,Allow
1.1.1.1,Deny
```

## Usage

```shell
python3 generate-htaccess.py
# or
./generate-htaccess.py
```

## TODO

- Argparse and environment configuration
- Unit Test
- Gitlab-CI settings
