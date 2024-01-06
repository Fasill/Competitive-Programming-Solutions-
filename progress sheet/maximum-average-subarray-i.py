class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
                
        w = nums[0:k]
        s = sum(w)
        m = s / k
        if len(nums) == 1:
            return m
        l = 1
        r = k+1
        ms = s
        while r<len(nums)+1:
            s = (s-nums[l-1])+nums[r-1]
            ms = max(s,ms)
            l+=1
            r+=1
        return ms/k



        return max_av