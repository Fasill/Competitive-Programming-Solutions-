class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums)
        _sum = sum(nums)
        nums = nums[::-1]
        for i in range(len(nums)):
            _sum -= nums[i]
            if _sum > nums[i]:
                print(i,nums[i])
                return _sum+nums[i]
        return -1