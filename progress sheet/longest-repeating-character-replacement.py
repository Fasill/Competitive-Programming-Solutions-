class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = defaultdict(int)
        l= 0
        s = list(s)
        n = len(s)
        maxFre = float('-inf')
        maxLeng = 0

        for r in range(n):
            
            d[s[r]]+=1
            maxFre = max(maxFre,d[s[r]])

            while (r-l+1)-maxFre>k:
                d[s[l]]-=1
                l+=1
            maxLeng=  max(maxLeng,r-l+1)
        return maxLeng

