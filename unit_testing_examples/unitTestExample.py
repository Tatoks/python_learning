import unittest


def add(x, y):
    return x + y


def div(x, y):
    return x / y


def sub(x, y):
    return x - y


def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)


# MyTest inherits TestCase class from unittest
class MyTest(unittest.TestCase):

    def setUp(self):
        print("IN SET UP")

    def tearDown(self) -> None:
        print("IN TEAR DOWN")

    def test_add(self):
        self.assertEqual(add(3, 4), 7)

    def test_sub(self):
        self.assertEqual(sub(10, 5), 5)

    def test_factorial(self):
        res = fact(5)
        self.assertEqual(res, 120)

    def test_zerodivisionerror(self):
        with self.assertRaises(ZeroDivisionError): 6 / 0

    def test_zerodivisionerrorB(self):
        self.assertRaises(ZeroDivisionError, div, 8, 0)

    def test_split(self):
        s = 'hello$$sorld'
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(4)


# Executing the script as standalone, the __name__ will equal to __main__
# unittest.main() will execute all tests methods that you wrote


if __name__ == '__main__':
    unittest.main()
