class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        def FlipAndInvert(nums):
            nums = nums[::-1]
            for i in range(len(nums)):
                if nums[i] == 0:
                    nums[i] = 1
                elif nums[i] == 1:
                    nums[i] = 0
            return nums
        ans = []
        for i in image:
            ans.append(FlipAndInvert(i))
        return ans
        