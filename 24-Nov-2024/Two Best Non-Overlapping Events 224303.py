# Problem: Two Best Non-Overlapping Events - https://leetcode.com/problems/two-best-non-overlapping-events/

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        
        mx, ans = 0, 0

        beg, end, val = zip(*events)
        beg2ndMtg = sorted(zip(beg, val))
        end1stMtg = iter(sorted(zip(end, val)))

        end1st, val1st = next(end1stMtg)

        for beg2nd, val2nd in beg2ndMtg:

            while end1st < beg2nd:
                mx = max(mx, val1st)
                end1st, val1st = next(end1stMtg)

            ans = max(ans, mx + val2nd)

        return ans  