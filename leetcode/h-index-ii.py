class Solution:
    def hIndex(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        ans = 0
        n = len(nums)
        while l<=r:
            mid = l + (r-l) // 2
            # print( nums[mid], r-mid + 1 )
            if nums[mid]< n-mid :
                l = mid + 1
            
            else:
                r = mid - 1
                ans = n-mid 

        return ans