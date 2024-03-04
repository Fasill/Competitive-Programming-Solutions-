class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subset = [[]]
        cur = []
        n = len(nums)
        _set = set()
        def track(i,cur):
            if i <= n:
                cur = sorted(cur)
                
                if cur not in subset: 
                    subset.append(cur[:])
                
            else:
                return

            for j in range(i,n):
                cur.append(nums[j])
               
                track(j+1,cur)
                cur.pop()
        track(0,[])
        return subset