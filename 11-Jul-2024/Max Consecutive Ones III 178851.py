# Problem: Max Consecutive Ones III - https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0

        longesOnes = 0
        _max = 0
        while r < len(nums):
            if nums[r] == 0:
                longesOnes += 1
            while longesOnes > k:
                if nums[l] == 0:
                    longesOnes -= 1
                l += 1
            _max = max(_max, (r-l) + 1)
            r += 1
        return _max
