import unittest

from client import getRatio
class TestZeroDivision(unittest.TestCase):
    def test_zerodivison(self):
        with self.assertRaises(ZeroDivisionError):
            getRatio(110,0)

if __name__ =='__main__':
    unittest.main()