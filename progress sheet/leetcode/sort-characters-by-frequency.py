class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        c = dict(sorted(c.items(), key=lambda x:x[1],reverse=True))
        s = []
        for i in c:
            s .append(i*c[i])
        
        return "".join(s)