class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeroCounter = 0
        left = 0
        maxLength = 0
        arrayLengh = len(nums)
        for right in range(arrayLengh):

            if nums[right] == 0:
                zeroCounter += 1

            while zeroCounter > k:
                if nums[left] == 0:
                    zeroCounter -= 1
                left += 1

            maxLength = max(maxLength,right-left+1) 
        return maxLength