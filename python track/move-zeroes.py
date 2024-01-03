class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l,r  = 0,1
        while r<len(nums):
            if nums[l] == 0 and nums[r] != 0:
                nums[l],nums[r] = nums[r],nums[l]
          
            elif nums[l] == 0 and nums[r] == 0:
                r+=1
            else:
                r+=1
                l+=1




                