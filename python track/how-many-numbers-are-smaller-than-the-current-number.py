class Solution:
    def countNums(self,nums,target):
        i,j = 0,len(nums)-1
        nums = sorted(nums)
        c = 0
        while nums[i] != target:
            c+=1
            i+=1
        return c
        
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            ans.append(self.countNums(nums,i))
        return ans