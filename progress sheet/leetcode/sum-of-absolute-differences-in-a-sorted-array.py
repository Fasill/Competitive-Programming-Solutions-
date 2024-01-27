class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        leftSum = 0
        
        totalSum = sum(nums)
        n = len(nums)
        ans = []
        for i in range(n):
            rightSum = totalSum- nums[i]-leftSum

            left = nums[i]*i-leftSum
            right = rightSum-nums[i]*(n-i-1)

            ans.append(left+right)
            leftSum += nums[i]
        
        return ans

