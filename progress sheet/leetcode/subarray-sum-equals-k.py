class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prifixSum = {0:1}
        n = len(nums)
        c = 0
        _sum = 0

        for r in range(n):
            _sum += nums[r]
            if _sum-k in prifixSum:
                c+=prifixSum[_sum-k]
            if _sum in prifixSum:
                prifixSum[_sum]+=1
            else:
                 prifixSum[_sum] = 1

        return c
            