import unittest
from task import findLucky

class TestAssignment(unittest.TestCase):

    def test_single_digit(self):
        self.assertEqual(findLucky([2,2,3,4]), 2)

    def test_multiple_digits(self):
        self.assertEqual(findLucky([1,2,2,3,3,3]),3)

    def test_with_zero(self):
        self.assertEqual(findLucky([2,2,2,3,3]),-1)

if __name__ == "__main__":
    unittest.main()
