# Introduction au modèle objet en Python

Dans le cadre du scripting Python pour un DevOps, vous aurez rarement l'occasion d'utiliser la programmation Objet mais il peut être utile d'en comprendre les bases pour analyser un code.

## Les classes

**Un exemple de pseudo code sans classe:**

```python
import sqlite3

def connect_db(filepath):
    return sqlite3.connect(filepath)

def create_tables(db):
    c = db.cursor()
    c.execute('''CREATE TABLE contacts (first_name text, last_name text)''')

def insert_data(db, first_name, last_name):
    c = db.cursor()
    c.execute(f"INSERT INTO contacts VALUES ({first_name}, {last_name})")
    db.commit()

def main():
    db = connect_db("example.db")
    create_tables(db)
    insert_data(db, "Alain", "DURANT")
    db.close()
```

**Le même code avec une classe:**

```python
import sqlite3

class DAO:

    def __init__(self, filepath):
        self.filepath = filepath
        self.db = self.connect_db()
        self.create_tables()

    def connect_db(self):
        return sqlite3.connect(self.filepath)

    def create_tables(self):
        c = self.db.cursor()
        c.execute("CREATE TABLE contacts (first_name text, last_name text)")

    def insert_data(self, first_name, last_name):
        c = self.db.cursor()
        c.execute(f"INSERT INTO contacts VALUES ({first_name}, {last_name})")
        self.db.commit()

def main():
    dao = DAO("example.db")
    dao.insert_data("Alain", "DURANT")
    dao.db.close()
```

**Explications:**

- Chaque méthode à l'intérieur d'une classe commence par un paramètre **self**
- La méthode spéciale **__init__** permet d'initialiser l'instance de la classe
- Les fonctions SQL, accèdent directement à self.db

## Classe et instances de classe

TODO...

## L'héritage

TODO...

## Les méthodes (fonctions) et attributs

La terminologie avec le modèle objet est différent mais le fonctionnement reste le même.

- Une fonction devient une méthode
- Une variable devient un attribut

## Méthodes et attributs de classe ou d'instance

TODO...



