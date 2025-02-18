import sys
import unittest
from math import factorial as math_factorial

from exercises.calculate_factorial import factorial_recursive, process_input, factorial_iterative, \
    factorial_iterative_recursive


class TestFactorial(unittest.TestCase):
    # Test factorial_recursive method
    def test_factorialRecursiveOnZero(self):
        self.assertEqual(factorial_recursive(0), 1)

    def test_factorialRecursiveOnOne(self):
        self.assertEqual(factorial_recursive(1), 1)

    def test_factorialRecursiveOnPositiveNumber(self):
        self.assertEqual(factorial_recursive(2), 2)
        self.assertEqual(factorial_recursive(5), 120)

    def test_factorialRecursiveOnLargeNumber(self):
        self.assertEqual(factorial_recursive(12), 479001600)
        self.assertEqual(factorial_recursive(14), 87178291200)


    # Test factorial_iterative method
    def test_factorialIterativeOnZero(self):
        self.assertEqual(factorial_iterative(0), 1)

    def test_factorialIterativeOnOne(self):
        self.assertEqual(factorial_iterative(1), 1)

    def test_factorialIterativeOnPositiveNumber(self):
        self.assertEqual(factorial_iterative(2), 2)
        self.assertEqual(factorial_iterative(5), 120)

    def test_factorialIterativeOnLargeNumber(self):
        self.assertEqual(factorial_iterative(12), 479001600)
        self.assertEqual(factorial_iterative(14), 87178291200)


    # Test factorial_iterative_recursive method
    def test_factorialIterativeRecursiveBeforeRecursionLimit(self):
        limit = sys.getrecursionlimit() - 1
        result = factorial_iterative_recursive(limit)
        expected = math_factorial(limit)
        self.assertEqual(result, expected)

    def test_factorialIterativeRecursiveAfterRecursionLimit(self):
        limit = sys.getrecursionlimit() + 1
        result = factorial_iterative_recursive(limit)
        expected = math_factorial(limit)
        self.assertEqual(result, expected)


    # Test process_input method
    def test_processInputOnValid(self):
        self.assertEqual(process_input("1"), (1, False, None))

    def test_processInputOnNegative(self):
        self.assertEqual(process_input("-3"),
                         (None, True, "Your number is out of the correct range. Please try again."))

    def test_processInputOnFraction(self):
        self.assertEqual(process_input("3/4"),
                         (None, True, "Invalid entry. Please try again."))


if __name__ == '__main__':
    unittest.main()
