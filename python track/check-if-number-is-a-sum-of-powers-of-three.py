from math import *
class Solution(object):
    def checkPowersOfThree(self, n):
        while n>0:
            if n%3 == 2:
                return False
            else:
                n = n/3
        return True