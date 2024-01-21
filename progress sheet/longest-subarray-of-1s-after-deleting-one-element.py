class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zeroCounter = 0
        left = 0
        arrayLength = len(nums)
        longestArray = 0

        for right in range(arrayLength):
            if nums[right] == 0:
                zeroCounter+=1
                
            while zeroCounter >1:
                if nums[left] == 0:
                    zeroCounter-=1
                left += 1
            longestArray = max(longestArray,(right-left))

        return longestArray            


