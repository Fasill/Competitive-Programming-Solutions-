# Problem: First Missing Positive - https://leetcode.com/problems/first-missing-positive/description/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        ref = set(nums)
        _max = 2 ** 31


        for num in range(1, _max ):
            if num not in ref:
                return num

