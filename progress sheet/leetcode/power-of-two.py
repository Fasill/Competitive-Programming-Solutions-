class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        return int(log2(n)) == log2(n)