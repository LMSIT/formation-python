# Le module argparse pour des options en ligne de commande

## sys.argv

```python
import sys

if len(sys.argv) < 2:
    print("error: host parameter require")
    print("example: %s 1.1.1.1 8080" % sys.argv[0])
    sys.exit(1)

if len(sys.argv) < 3:
    print("error: port parameter require")
    print("example: %s 1.1.1.1 8080" % sys.argv[0])
    sys.exit(1)

host = sys.argv[1]
port = int(sys.argv[2])

print("%s:%s" % (host, port))
```

## Module argparse

> **argparse** est inclus en standard avec Python

- https://docs.python.org/fr/3/howto/argparse.html
- https://docs.python.org/3/library/argparse.html

```python
import argparse
parser = argparse.ArgumentParser()

parser.add_argument('--host', '-H',
                                dest='host',
                                help='Host Address. Default: %(default)s',
                                default='127.0.0.1',
                                required=True)

parser.add_argument('--port',
                                dest='port',
                                help='Host Port. Default: %(default)s',
                                default=8080,
                                required=False)

args = parser.parse_args()

print("%s:%s" % (args.host, args.port))
```

## Addons click

[click](https://click.palletsprojects.com/) est une librairie dédié à la définition d'options en ligne de commande. L'outil a été développé par les mêmes auteurs que le framework [Flask](https://flask.palletsprojects.com/)

```shell
pip install click
```

```python
import click

@click.command()
@click.option('--host', '-H', default='127.0.0.1', help='Host Address.', show_default=True)
@click.option('--port', default=8080, type=click.IntRange(1024, 65000), help='Host port.', show_default=True)
def host_port(host, port):
    """Host and port options."""
    click.echo('%s:%s' % (host, port))

if __name__ == '__main__':
    host_port()

```

