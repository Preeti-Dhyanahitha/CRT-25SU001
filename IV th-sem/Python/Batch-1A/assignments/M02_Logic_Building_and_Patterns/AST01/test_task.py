import unittest
from task import isUgly

class TestAssignment(unittest.TestCase):

    def test_single_digit(self):
        self.assertEqual(isUgly(6), True)

    def test_multiple_digits(self):
        self.assertEqual(isUgly(1), True)

    def test_with_zero(self):
        self.assertEqual(isUgly(14), False)

if __name__ == "__main__":
    unittest.main()
