class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n =  int(len(nums)/3)
        x = []
        for i in set(nums):
            if  nums.count(i) > n:
                x.append(i)
        return x