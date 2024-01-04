class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
  
        l,r = 0,1
     
        k = len(set(nums))

        if k == len(nums):
            return k

        while l<k:
            if nums[l] == nums[r]:
                nums.append("_")
                nums.pop(r)
            else:
                l+=1
                r+=1
        return k

        
