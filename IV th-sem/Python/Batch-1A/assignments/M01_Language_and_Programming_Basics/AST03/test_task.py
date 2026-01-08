import unittest
from task import sum_of_digits

class TestAssignment(unittest.TestCase):

    def test_single_digit(self):
        self.assertEqual(sum_of_digits(5), 5)

    def test_multiple_digits(self):
        self.assertEqual(sum_of_digits(1234), 10)

    def test_with_zero(self):
        self.assertEqual(sum_of_digits(1010), 1)

if __name__ == "__main__":
    unittest.main()
