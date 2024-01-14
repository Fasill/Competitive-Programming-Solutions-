
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        l =0
        r = 0
        _max = 0
        z = 1

        while r < n:
            if nums[r] == 0:
                z -= 1

            while z < 0:
                if nums[l] == 0:
                    z += 1
                l += 1
                

            _max = max(_max, r - l )
            r += 1

        return _max  