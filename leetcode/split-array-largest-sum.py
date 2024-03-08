class Solution:
    def helper(self,nums,_sum):
        n = 0
        temp = 0
        for i in range(len(nums)):
            if temp + nums[i] > _sum:
                n += 1
                temp = nums[i]
            else:
                temp += nums[i]
        return n+1
    

    def splitArray(self, nums: List[int], k: int) -> int:

        left, right = max(nums),sum(nums)
        
        ans = left
        while left <= right:
            mid = left + (right-left) // 2

            num = self.helper(nums,mid)
            if num > k:
                left = mid + 1
            else:
                right = mid - 1
                ans = mid
        
        return ans