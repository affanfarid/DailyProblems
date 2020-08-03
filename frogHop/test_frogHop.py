import unittest
import frogHop

class TestCalc(unittest.TestCase):
    def test_frogHop(self):
        self.assertEqual(frogHop.frogHop([0,1,3,5,6,8,12,17]),True)
        self.assertEqual(frogHop.frogHop([0,1,2,3,4,8,9,11]),False)
        self.assertEqual(frogHop.frogHop([0,1,3,6,10,15,21]),True)
        self.assertEqual(frogHop.frogHop([num for num in range(0,100)]),True)


if __name__ == '__main__':
    unittest.main()
