import unittest
<<<<<<< HEAD
from task import findLucky

class TestAssignment(unittest.TestCase):

    def test_single_digit(self):
        self.assertEqual(findLucky([2,2,3,4]), 2)

    def test_multiple_digits(self):
        self.assertEqual(findLucky([1,2,2,3,3,3]),3)

    def test_with_zero(self):
        self.assertEqual(findLucky([2,2,2,3,3]),-1)
=======
from task import reverse_number

class TestAssignment(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(reverse_number(123), 321)

    def test_two_digits(self):
        self.assertEqual(reverse_number(45), 54)

    def test_zero_end(self):
        self.assertEqual(reverse_number(120), 21)
>>>>>>> ca8183368301e9e2cda1fbc95a57a18121070cd1

if __name__ == "__main__":
    unittest.main()
