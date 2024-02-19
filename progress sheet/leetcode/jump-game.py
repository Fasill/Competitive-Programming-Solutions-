class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cur = 1
        for i in range(len(nums)-1):
            cur-=1
            if cur == 0 and nums[i] == 0:
                return False
            
            cur = max(cur, nums[i])

        return True