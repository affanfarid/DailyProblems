import unittest
import longestMountain

class TestLongestMountain(unittest.TestCase):
    def test_longestMountain(self):
        self.assertEqual(longestMountain.longestMountain( [] ), 0 )
        self.assertEqual(longestMountain.longestMountain( [2,1,4,7,3,2,5] ), 5 )
        self.assertEqual(longestMountain.longestMountain( [1,3,2] ), 3 )
        self.assertEqual(longestMountain.longestMountain( [5,1,2,3,2,5] ), 4 )
        self.assertEqual(longestMountain.longestMountain( [1,5,1,5] ), 3 )
        self.assertEqual(longestMountain.longestMountain( [5,1,5,1] ), 3 )
    def test_longestMountainPlataeu(self):
        self.assertEqual(longestMountain.longestMountain( [2,2,2] ), 0 )
        self.assertEqual(longestMountain.longestMountain( [1,1,2,2] ), 0 )
        self.assertEqual(longestMountain.longestMountain( [1,5,2,2] ), 3 )
        self.assertEqual(longestMountain.longestMountain( [1,2,2,3] ), 0 )
        self.assertEqual(longestMountain.longestMountain( [1,2,2,1] ), 0 )
        self.assertEqual(longestMountain.longestMountain( [1,2,3,2,2,1] ), 4 )

        

if __name__ == '__main__':
    unittest.main()