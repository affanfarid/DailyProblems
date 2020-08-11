import unittest
import smashRocks

class TestSmashRocks(unittest.TestCase):
    def test_smashRocks(self):
        self.assertEqual(smashRocks.smashRocks( [2,7,4,1,8,1]), 1 )
        self.assertEqual(smashRocks.smashRocks( [2,7,4,1,8]),   0 )
        self.assertEqual(smashRocks.smashRocks( [] ), 0 )
        self.assertEqual(smashRocks.smashRocks( [6,7,8] ), 5 )
        self.assertEqual(smashRocks.smashRocks( [10,9,8,7,6,5,4,3,2,1] ), 1 )
        self.assertEqual(smashRocks.smashRocks( [100,1]), 99 )



if __name__ == '__main__':
    unittest.main()