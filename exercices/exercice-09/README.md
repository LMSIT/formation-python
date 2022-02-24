# Htaccess file generator

This tool is used to generate an [.htaccess](http://httpd.apache.org/docs/current/howto/htaccess.html) file for Apache from a CSV file containing IP addresses and rules.

## Requirements

- Python 3.5+

## Installation

```shell
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip wheel
pip install jinja2
```

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

# for choice options
./generate-htaccess.py --help

# Use environment variable for htaccess path:
LBN_OUTPUT_FILENAME=/etc/httpd/.htaccess ./generate-htaccess.py
```

## Run tests

```shell
# Run all tests with main function
python3 test_generate_htaccess.py

# Run all tests with unittest module
python3 -m unittest test_generate_htaccess

# Run all tests of TestHtaccess class
python3 -m unittest test_generate_htaccess.TestHtaccess

# Run test_render_template() method only
python3 -m unittest -v test_generate_htaccess.TestHtaccess.test_render_template
```

## TODO

- Gitlab-CI settings
