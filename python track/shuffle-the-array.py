class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        left  = nums[:n].copy()
        right  = nums[n:].copy()
        ans = []
        for i in range(n):
            ans.append(left[i])
            ans.append(right[i])
        return ans

            
