# Exécution de commandes systèmes

## Avec subprocess

```python
import subprocess

cmd = "ls -l /"
result = subprocess.run(cmd, shell=True, check=True, capture_output=True)

print("SUCCESS : ", result.returncode == 0)

print(result.stdout)
```

## Avec PyInvoke

> Avec l'extension [invoke](https://www.pyinvoke.org/)
```shell
$ pip install invoke
```

```python
from invoke import run
cmd = "ls -l /"
result = run(cmd, hide=True, warn=True)

print("SUCCESS : ", result.ok)

for line in result.stdout.splitlines():
    print(line)
```

