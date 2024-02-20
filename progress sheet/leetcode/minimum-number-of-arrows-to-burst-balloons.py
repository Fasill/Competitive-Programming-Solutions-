class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n = len(points)
        nums = sorted(points, key = lambda x:x[0])
        prev = nums[0]
        arrows = 1
        print(nums)
        for i in range(1,n):


            if prev[-1] < nums[i][0]:
                arrows += 1
                prev = nums[i]
            else: 
                prev = [nums[i][0],min(prev[1],nums[i][1])]
        return arrows

