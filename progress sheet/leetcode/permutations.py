class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        cur = []
        n = len(nums)
        def track(i):
            if i == n:
                if len(set(cur)) == n:
                    ans.append(cur[:])
                return
            
            for j in range(n):
                
                
                cur.append(nums[j])
                track(i+1)
                cur.pop()
        track(0)
        return ans