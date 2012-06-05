import unittest
from fizzbuzz import FizzBuzz

class TestFizzBuzz(unittest.TestCase):

	def test_simple(self):
		self.assertEqual(FizzBuzz(1), 1)
		self.assertEqual(FizzBuzz(2), 2)
		self.assertEqual(FizzBuzz(4), 4)
		

if __name__ == '__main__':
	unittest.main()