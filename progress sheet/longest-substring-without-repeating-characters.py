class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = defaultdict(int)
        l = 0
        n = len(s)
        maxLeng = 0
        for r in range(n):
            d[s[r]] +=1
            while  d[s[r]] > 1:
                d[s[l]] -= 1
                l+=1

            maxLeng = max(maxLeng,r-l+1)
        return maxLeng
            

    
        