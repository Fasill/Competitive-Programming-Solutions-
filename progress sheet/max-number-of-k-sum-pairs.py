class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
            l = 0
            r = len(nums)-1
            c = 0
            nums = sorted(nums)

            while l<r:
                if nums[l]+nums[r] == k:
                    c+=1
                    l+=1
                    r-=1
                elif  nums[l]+nums[r] >k:
                    r-=1

                elif nums[l] + nums[r] < k:
                    l += 1

            return c