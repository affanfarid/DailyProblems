import unittest
import astroids

class TestCalc(unittest.TestCase):
    def test_astroid(self):
        self.assertEqual( astroids.astroids( [5, 10, -5] ) ,[5, 10])
        self.assertEqual( astroids.astroids( [8, -8] ) , [])
        self.assertEqual( astroids.astroids( [10, 2, -5]) , [10])
        self.assertEqual( astroids.astroids( [-2, -1, 1, 2] ) , [-2, -1, 1, 2])
        self.assertEqual( astroids.astroids( [8,1,2,3,4,5,6,7,-8]) , [])
        self.assertEqual( astroids.astroids( [8, -7, -6, -5, -4, -8] ) , [])

if __name__ == '__main__':
    unittest.main()