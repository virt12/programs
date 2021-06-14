import unittest
import sys
import string
from Solution import Solution


class NamesTestCase(unittest.TestCase):

    def test_longest(self):
       s=Solution()
       result = s.longest("bbbbb")
       self.assertEqual(result, (1, 'b'))
    
    def test_longest2(self):
       s=Solution()
       result = s.longest("abcabcbb")
       self.assertEqual(result, (3, 'abc'))
    
    def test_longest3(self):
       s=Solution()
       result = s.longest("pwwkew")
       self.assertEqual(result, (3, 'wke'))



unittest.main()