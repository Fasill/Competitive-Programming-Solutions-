class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        d = {}
        for i, j in zip(s, indices):
            d[j] = i
        y = sorted(d)
        x = ''
        for i in y:
            x += d[i]
        return x

