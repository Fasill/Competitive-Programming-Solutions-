class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cur = nums[0]
        if len(nums) == 1:
            return True
        if cur == 0:
            return False

        for i in range(1,len(nums)):
            cur -= 1
            cur = max(nums[i],cur)
            if cur <1 and i != len(nums)-1:
                return False
        return True
