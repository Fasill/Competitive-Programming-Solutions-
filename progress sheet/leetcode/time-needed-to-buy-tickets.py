class Solution:
    def timeRequiredToBuy(self, nums: List[int], k: int) -> int:
        counter = 0
        target = nums[k]
        for num in nums:
            if num>target:
                counter += target
            else:
                counter+=num
        for i in range(k+1,len(nums)):
            if nums[i] >= target:
               counter -= 1
             
        return counter