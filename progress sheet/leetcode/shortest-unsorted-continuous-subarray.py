class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # copy the elements
        cop = nums.copy()
        # sort the copy nums
        cop.sort()
        
        # get the position of the elements where they should be
        sorted_indx = {i:x for i,x in enumerate(cop)}
        
        unsorted_indx = {i:x for i,x in enumerate(nums)}
        
        left = 0
        right = len(nums)-1
        # check for the first and the last element if they are on their posetion
        for i in range(len(nums)):
            if sorted_indx[left] == unsorted_indx[left]:
                left +=1
                
            if sorted_indx[right] == unsorted_indx[right]:
                right -=1
        if nums == sorted(nums):
            return 0
        return right - left + 1