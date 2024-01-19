class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(1,len(nums)+1):
            j = sum(nums[:i])
            res.append(j)
        return res