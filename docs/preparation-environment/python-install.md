# Installation de Python

Quelque soit votre OS, utilisez la version de 3.6.8 au minimum car les versions antérieurs ne sont plus maintenus.

## Windows 10

Avec Windows 10, vous avez plusieurs choix:
- Utiliser WSL2 pour charger une distribution Linux. Voir la [documentation](https://docs.microsoft.com/fr-fr/windows/wsl/install-win10)
- Installer le package Python pour Windows en le téléchargeant à partir d'[ici](https://www.python.org/downloads/)
- Créer une machine virtuelle Ubuntu avec [Multipass](https://multipass.run/)
- Installer Linux dans une VirtualBox

## Linux Ubuntu/Debian

- Vérifiez d'abord quelle version est installé: `python -V` ou `python3 -V`

Si la version 3 n'est pas installé ou trop ancienne:

```shell
sudo apt-get update
sudo apt-get install python3 python3-venv
```

Pour plus d'options et d'information: https://docs.python-guide.org/starting/install3/linux/

## Linux Redhat


**Depuis Redhat 8 / Centos 8, `dnf` remplace `yum`:**

```shell
sudo dnf install python3
```

**Pour les anciennes versions de Redhat, vous devrez peut être utiliser les softwares collections:**

> TODO: Cette partie est à vérifier

```shell
# centos:
yum install centos-release-scl

# fedora 
sudo yum install rh-python36
scl enable rh-python36 bash
```

Pour plus d'options et d'information: https://docs.python-guide.org/starting/install3/linux/

## Docker

Si vous avez Docker ou [Podman](https://podman.io/), vous pouvez utiliser un conteneur qui contient déjà Python.

```shell
docker run -it --rm -v $PWD:/code -w /code python:3.6.12-alpine sh
```
