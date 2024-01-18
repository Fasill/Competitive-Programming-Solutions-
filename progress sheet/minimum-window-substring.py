class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = Counter(t)
        s_count = Counter()
        l = 0
        min_leng = float('inf')
        st = ""
        n = len(s)
        for r in range(n):
            s_count[s[r]]+=1
            while t_count-s_count == Counter():
                if min_leng >r-l+1:
                    min_leng = r-l+1
                    st = s[l:r+1]
                s_count[s[l]]-=1
                l+=1
        return st