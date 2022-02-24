# Introduction aux tests unitaires

Comme le nom l'indique, un test unitaire sert à tester unitairement de petits bout de code.

Le plus souvent, il y aura un test par fonction, regroupé par module. 

**Exemple de test écrit avec unittest:**

```python
# calculs.py
def add(a, b):
    return a+b

def multiply(a, b):
    # TODO: multiply function
    pass

# test_calculs.py
import unittest
import calculs

class TestCalculs(unittest.TestCase):

    def test_add(self):
        sum = calculs.add(1, 2)
        self.assertEqual(sum, 3)

    def test_multiply(self):
        self.fail("Not Implemented function")

```

**Exécution des tests avec le module unittest:**

```shell
python3 -m unittest -v test_calculs.py
test_add (test_calculs.TestCalculs) ... ok
test_multiply (test_calculs.TestCalculs) ... FAIL

======================================================================
FAIL: test_multiply (test_calculs.TestCalculs)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/tmp/test_calculs.py", line 11, in test_multiply
    self.fail("Not Implemented function")
AssertionError: Not Implemented function

----------------------------------------------------------------------
Ran 2 tests in 0.001s

FAILED (failures=1)
```

> Python fournit un module standard pour les tests qui se nomme [unittest](https://docs.python.org/fr/3.6/library/unittest.html) mais d'autres librairies existent, en particulier: [pytest](https://docs.pytest.org/)

**Installation et utilisation de pytest:**

```shell
pip install pytest

pytest test_calculs.py
=========================================================================== test session starts ============================================================================
platform linux -- Python 3.8.2, pytest-6.1.1, py-1.9.0, pluggy-0.13.1
rootdir: /tmp
collected 2 items

test_calculs.py .F                                                                                                                                                   [100%]

================================================================================= FAILURES =================================================================================
________________________________________________________________________ TestCalculs.test_multiply _________________________________________________________________________

self = <test_calculs.TestCalculs testMethod=test_multiply>

    def test_multiply(self):
>       self.fail("Not Implemented function")
E       AssertionError: Not Implemented function

test_calculs.py:11: AssertionError
========================================================================= short test summary info ==========================================================================
FAILED test_calculs.py::TestCalculs::test_multiply - AssertionError: Not Implemented function
======================================================================= 1 failed, 1 passed in 0.12s ========================================================================
```

**Ecriture du test au format pytest:**

> Les fonctions doivent obligatoirement commencer par **test_**

```python
# test_calculs.py
import unittest
import calculs

def test_add():
    sum = calculs.add(1, 2)
    assert sum == 3

def test_multiply():
    assert False "Not Implemented function"
```

