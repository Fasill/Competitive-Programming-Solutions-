class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def DnQ(s):
            if len(s) <=1:
                return ""
            uniqueS = set(s)
 
            c = 0
            for i in range(len(s)):
                if s[i].swapcase()  in uniqueS:
                    c+=1
            if c == len(s):
                return s

            for i in range(len(s)):
                if s[i].swapcase() not in uniqueS:
                    left = DnQ(s[:i])
                    right = DnQ(s[i+1:])
                    return max(left,right,key=len)
        return DnQ(s)
