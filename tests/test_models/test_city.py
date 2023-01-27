import unittest


def add(x, y):
    return x + y

class TestCity(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
    def fun_not_run(self):
        print("no run")
    def test_format(self):
        # Tests that work for only a certain version of the library.
        pass
    def test_windows_support(self):
        # windows specific testing code
        pass
    def test_add_two_positive_numbers(self):
        result = add(2, 3)
        self.assertEqual(result, 5)
    def test_add_two_negative_numbers(self):
        result = add(-2, -3)
        self.assertEqual(result, -5)


