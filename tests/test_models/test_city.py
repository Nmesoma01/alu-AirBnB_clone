import unittest
class TestCity(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
    def fun_not_run(self):
        print("no run")
        
