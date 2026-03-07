import unittest
from task import is_even

class TestAssignment(unittest.TestCase):

    def test_even_number(self):
        self.assertEqual(is_even(4), True)

    def test_odd_number(self):
        self.assertEqual(is_even(7), False)

    def test_zero(self):
        self.assertEqual(is_even(0), True)

if __name__ == "__main__":
    unittest.main()
