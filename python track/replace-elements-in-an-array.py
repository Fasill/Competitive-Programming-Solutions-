class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        d = {n: i for i, n in enumerate(nums)}
        
        for i in operations:
            r, n = i
            j = d[r]
            nums[j] = n
            d[n] = j
            del d[r]
            
        return nums
