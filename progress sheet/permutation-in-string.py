class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
            
        l = 0
        r = len(s1)
        while r<len(s2)+1:
            w = s2[l:r]
            if sorted(s1) == sorted(w):
                return True
            l+=1
            r+=1
        return False
