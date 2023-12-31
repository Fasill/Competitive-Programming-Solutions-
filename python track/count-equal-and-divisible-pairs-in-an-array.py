class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        l,r = 0,1
        c = 0
        while r<len(nums):
            if nums[l] == nums[r] and (l*r)%k == 0:
                print(l,r,l*r)
                c+=1
            if r == len(nums)-1:
                l+=1 
                r = l+1
            else:
                r+=1
        return c
                 

                
