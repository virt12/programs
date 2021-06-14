import sys
import string
import unittest
class Solution(object):
    def longest(self,phrase):
        max_sub = sub = ""
        for c in phrase:
            if c in sub:
                if len(sub) > len(max_sub):
                    max_sub = sub
                sub = sub[sub.find(c)+1:]
            sub += c
        if len(sub) > len(max_sub):
            max_sub = sub
        return (len(max_sub), max_sub)


if __name__=="__main__":
    ob1=Solution()
    print(ob1.longest(sys.argv[1]))
    











#print(longest("abcabcbb"))
#print(longest("bbbbb"))
#print(longest("pwwkew"))
#print(longest("helloworld"))