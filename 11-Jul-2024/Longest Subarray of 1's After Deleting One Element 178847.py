# Problem: Longest Subarray of 1's After Deleting One Element - https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zero  = 0
        ones = 1
        l,r = 0,0
        longest_non_empty = 0
        n = len(nums)
        for r in range(n):
            if nums[r] == 0:
                zero+=1
            else:ones+=1
            while zero>1:
                if nums[l] == 0:
                    zero -= 1
                else:
                    ones-=1
                l += 1
            longest_non_empty = max(longest_non_empty,(r-l))
        return longest_non_empty
