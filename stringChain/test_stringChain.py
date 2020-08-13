import unittest
import stringChain

class TestStringChain(unittest.TestCase):
    def test_validChain(self):
        self.assertEqual(stringChain.validChain2("ccc","cccc"), True )
        self.assertEqual(stringChain.validChain2("abba","abbba"), True )
        self.assertEqual(stringChain.validChain2("abba","aabba"), True )
        self.assertEqual(stringChain.validChain2("abba","abbca"), True )
        self.assertEqual(stringChain.validChain2("abba","cabba"), True )
        self.assertEqual(stringChain.validChain2("","a"), True )
        self.assertEqual(stringChain.validChain2("","ab"), False )
        self.assertEqual(stringChain.validChain2("abba","abba"), False )
        self.assertEqual(stringChain.validChain2("abba","abb"), False )
    def test_stringChain(self):
        self.assertEqual(stringChain.stringChain(["a","b","ba","bca","bda","bdca"]), 4)


if __name__ == '__main__':
    unittest.main()