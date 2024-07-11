# Problem: Longest Subarray of 1's After Deleting One Element - https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        r = 0

        maxZero = 0
        longestSubarray = 0
        while r < len(nums):
            if nums[r] == 0:
                maxZero += 1

            while maxZero > 1:
                if nums[l] == 0:
                    maxZero -= 1
                l += 1
             
            longestSubarray = max(longestSubarray,(r-l) + 1)
            r += 1
        return longestSubarray - 1