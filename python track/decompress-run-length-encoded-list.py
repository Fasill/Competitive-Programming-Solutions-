class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        l,r = 0,1
        x = []
        while r<len(nums):
            for i in range(nums[l]):
                x.append(nums[r])
            l = r+1
            r+=2
        return x
