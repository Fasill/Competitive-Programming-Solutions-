class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l,r = 0,0
        _max = float('-inf')
        for r,n in enumerate(nums):
           
            k-= 1-n

            if k < 0:
                k+=1-nums[l]
                l+=1
            r+=1
            _max = max(_max,r-l)
        return _max