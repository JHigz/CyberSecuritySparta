import unittest
import calculator

class Calctest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(2, 5), 7)
        self.assertEqual(calculator.add(-6, 5), -1)
        self.assertEqual(calculator.add(0, 0), 0)
        self.assertEqual(calculator.add(-6, -6), -12)
