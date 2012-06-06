import unittest
from fizzbuzz import FizzBuzz

class TestFizzBuzz(unittest.TestCase):

	def test_simple_should_return_the_number(self):
		self.assertEqual(FizzBuzz(1), 1)
		self.assertEqual(FizzBuzz(2), 2)
		self.assertEqual(FizzBuzz(4), 4)

	def test_multiple_3_should_return_fizz(self):
		self.assertEqual(FizzBuzz(3), "fizz")
		self.assertEqual(FizzBuzz(9), "fizz")

	def test_multiple_5_should_return_buzz(self):
		self.assertEqual(FizzBuzz(5), "buzz")
		self.assertEqual(FizzBuzz(10), "buzz")
		

if __name__ == '__main__':
	unittest.main()