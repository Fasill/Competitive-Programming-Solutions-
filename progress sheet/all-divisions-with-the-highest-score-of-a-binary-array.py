class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        ones = sum(nums)
        zeros = 0
        _max = float('-inf')
        d = defaultdict(list)
        for i in range(len(nums)+1):

            
            _max = max(zeros+ones,_max)
            d[zeros+ones].append(i) 
            if i!=len(nums):
                if nums[i] == 0:
                    zeros += 1
                elif nums[i] == 1:
                    ones -= 1 
            
        return d[_max]
        
        
                    