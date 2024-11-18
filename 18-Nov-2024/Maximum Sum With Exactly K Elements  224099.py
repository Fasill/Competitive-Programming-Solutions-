# Problem: Maximum Sum With Exactly K Elements  - https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/description/

class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        x = max(nums)
        prev = x
        for j in range(k-1):
            prev += 1
            x += prev
        return x
