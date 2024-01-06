class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        flag = True
        c = 0
        n = len(nums)
        if n == 1:
            return
        while flag:
            l,r = 0,1
            while r<n:
                if nums[l]>nums[r]:
                    nums[l],nums[r] = nums[r],nums[l]
                    c = 0
                else:
                    c+=1
                if c == n:
                    flag = False
                l+=1
                r+=1

        