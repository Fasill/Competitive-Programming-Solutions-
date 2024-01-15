class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        d = defaultdict(int)
        l= 0
        n = len(nums)
        maxSum = 0
        for r in range(n):
            d[nums[r]]+=1
            while  d[nums[r]]>1:
                d[nums[l]] -= 1
                l+=1

            maxSum = max(maxSum,sum(nums[l:r+1]))
        return maxSum
            