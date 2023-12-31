class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x = []
        for i in points:
            x.append(i[0])
        x = sorted(x)

        l, r = 0, 1
        m = 0
        while r < len(x):
            m = max(x[r] - x[l], m)
            l += 1
            r += 1
        return m
