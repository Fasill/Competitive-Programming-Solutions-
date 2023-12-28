class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        # l = 0
        c = 0
        if sorted(nums) == nums:
            return True

        for i in range(1,len(nums)):
            if nums[i-1]>nums[i]:
                t = nums[i-1]
                nums[i-1] = nums[i]
                if sorted(nums) == nums:
                    return True
                nums[i-1],nums[i] = t,t
                if sorted(nums) == nums:
                    return True
                return False
         