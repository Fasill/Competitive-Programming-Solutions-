class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        answer = 0
        for i in range(len(nums)-2,-1,-1):
            if nums[i]>nums[i+1]:
                nd = ceil(nums[i]/nums[i+1])
                answer += nd-1
                nums[i] = nums[i]//nd
                
        return answer
