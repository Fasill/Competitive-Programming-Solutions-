# Problem: Find Indices With Index and Value Difference I - https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/description/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def calcHash(sub):
            needleHashVal = 0
            for i in range(len(sub)):
               needleHashVal += (ord(sub[i])-96) * (27 ** ((len(sub) -1) -i))
            return  needleHashVal
        def pollFirst( hashedVal, s):
            return hashedVal - (ord(s)-96) * (27 ** (m-1))
        def addLast(hashedVal,s):
            return (hashedVal * 27) + (ord(s)-96) 

        needleHashVal = calcHash(needle)

        # needleHashVal %= (10**9) + 7

        l = 0
        r = len(needle) - 1
        n = len(haystack)
        m = len(needle)
        window = calcHash(haystack[:r+1])
        while r < n:
            if window  == needleHashVal :
                return l
            window = pollFirst( window, haystack[l])
            r += 1
            # if r <= n:
            #     return -1
            if r<n:
                window = addLast(window, haystack[r])
            l += 1
        return -1