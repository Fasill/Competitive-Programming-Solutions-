class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        n = len(nums)
        for i in range(2, n):
            k = 0
            for j in range(i - 1, 0, -1):
                while k < j and nums[k] + nums[j] <= nums[i]:
                    k += 1
                ans += max(j - k, 0)
        return ans