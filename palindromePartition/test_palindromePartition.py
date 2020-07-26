import unittest
import palindromePartition

class TestCalc(unittest.TestCase):
  def test_palindrome(self):
    self.assertEqual( palindromePartition.isPalindrome("aabaa"), True)
    self.assertEqual( palindromePartition.isPalindrome("aaaa"), True)
    self.assertEqual( palindromePartition.isPalindrome("ab"), False)

  def test_palPart(self):
    self.assertEqual (len(palindromePartition.palPart("ab")) , 1)
    self.assertEqual (len(palindromePartition.palPart("aba")) , 2)
    self.assertEqual (len(palindromePartition.palPart("aab")) , 2)
    self.assertEqual (len(palindromePartition.palPart("aaba")) , 3)



if __name__ == '__main__':
  unittest.main()