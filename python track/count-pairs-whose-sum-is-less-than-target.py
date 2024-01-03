from typing import List

class Solution:
   
    def countPairs(self, nums: List[int], target: int) -> int:
        c = 0

        # Sorting the array using bubbleSort
        nums =sorted(nums)

        l, r = 0, len(nums)-1
        while l < r:
            if nums[l] + nums[r] < target:
                c += (r - l)
                l += 1
            else:
                r -= 1
        return c
