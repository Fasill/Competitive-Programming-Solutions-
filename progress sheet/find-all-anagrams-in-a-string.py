class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l ,r= 0,len(p)
        p = list(p)

        p = sorted(p)
        ans = []
        while r <= len(s):
            w = s[l:r]
            if sorted(w) == p:
                ans.append(l)
            l+=1
            r+=1
        return ans