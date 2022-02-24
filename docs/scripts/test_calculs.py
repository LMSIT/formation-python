import unittest
import calculs

class TestCalculs(unittest.TestCase):

    def test_add(self):
        sum = calculs.add(1, 2)
        self.assertEqual(sum, 3)

    def test_multiply(self):
        self.fail("Not Implemented function")

