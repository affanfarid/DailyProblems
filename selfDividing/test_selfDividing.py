import unittest
import selfDividing

class TestSelfDividing(unittest.TestCase):
    def test_isSelfDividng(self):
        self.assertEqual(selfDividing.isSelfDividing(128), True)
        self.assertEqual(selfDividing.isSelfDividing(0), False)
        self.assertEqual(selfDividing.isSelfDividing(100), False)
        self.assertEqual(selfDividing.isSelfDividing(15), True)
    def test_selfDividing(self):
        self.assertEqual(selfDividing.selfDividing(1,22),[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22] )


if __name__ == '__main__':
    unittest.main()