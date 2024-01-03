class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        c = 0
        mi = 0
        s = 0
        for i, flip in enumerate(flips):
            mi = max(mi, flip)
            s += 1

            if s == mi:
                c += 1

        return c