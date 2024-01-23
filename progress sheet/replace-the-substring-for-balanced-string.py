class Solution:
    def balancedString(self, s: str) -> int:
        d = {"Q":0,
             "W":0,
             "E":0,
             "R":0}
        di = Counter()
        length = len(s)
        n = length//4
        for p in range(length):
            d[s[p]] +=1
            if d[s[p]] > n:
                di[s[p]] += 1
                d[s[p]] -= 1
        if di == Counter():
            return 0

        wind = Counter()
        l = 0
        c = float('inf')
        for r in range(len(s)):
            wind[s[r]] += 1
            while di-wind == Counter() and r>=l:
                wind[s[l]] -= 1
                c  = min(c,r-l+1)
                l+=1
        return 0 if c == float('inf') else c