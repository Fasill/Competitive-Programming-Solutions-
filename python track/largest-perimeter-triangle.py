class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums)
        ans = 0
        i = len(nums)-1
        while i >1:
            if nums[i]<nums[i-1]+nums[i-2]:
                ans = max(ans, nums[i]+nums[i-1]+nums[i-2])
            i-=1
            
        return ans