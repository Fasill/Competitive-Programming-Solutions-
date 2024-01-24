class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftSum = [0]
        for i in range(len(nums)-1):
            leftSum.append(leftSum[-1]+nums[i])
        rightSum = [0]
        for i in range(len(nums)-1,0,-1):
            rightSum.insert(0,rightSum[0]+nums[i])
        ans = []
        for i,j in zip(leftSum,rightSum):
            ans.append(abs(j-i))
        return ans