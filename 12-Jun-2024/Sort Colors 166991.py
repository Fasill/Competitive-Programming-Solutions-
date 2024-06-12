# Problem: Sort Colors - https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq = [0]*3
        for i in nums:
            freq[i] += 1

        for i in range(freq[0]):
            nums[i] = 0

        for i in range(freq[0] , freq[1] + freq[0]):
            nums[i] = 1

        for i in range(freq[1] + freq[0], freq[2] + freq[1] + freq[0]):
            nums[i] = 2
        
