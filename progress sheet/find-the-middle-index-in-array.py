class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        forPrifix = []
        n = len(nums)
        a = 0    
        for i in range(n):
            a+=nums[i]
            forPrifix.append(a)
        backPrifix = []
        a = 0
        for i in range(n-1,-1,-1):
            a += nums[i]
            backPrifix.append(a)
        print(backPrifix,forPrifix)
        backPrifix = backPrifix[::-1]
        for i in range(n):
            if backPrifix[i] == forPrifix[i]:
                return i
        return -1

