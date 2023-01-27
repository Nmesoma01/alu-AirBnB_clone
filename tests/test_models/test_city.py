import unittest
class TestCity(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
    def fun_not_run(self):
        print("no run")
    def test_nothing(self):
        self.fail("shouldn't happen")   
    def test_format(self):
        # Tests that work for only a certain version of the library.
        pass
    def test_windows_support(self):
        # windows specific testing code
        pass
