class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        bs = bisect_left(nums,target)
        br = bisect_right(nums,target)
        
        if bs>=len(nums) or nums[bs] != target:
            return [-1,-1]
        else:
            return [bs,br-1]
