class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        c = 0
        s = list(s)
        for r in range(1,len(s)+1):
            if len(set(s[l:r]))== len(s[l:r]):
                c+=1

            else: 
                l+=1
        return c
