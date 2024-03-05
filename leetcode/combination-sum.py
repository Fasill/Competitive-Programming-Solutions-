class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        cur = []
        n = len(candidates)
        def dfs(i,total):
            if total == target:
                res.append(cur[:])
                return
            if i >= n or total >  target:
                return
            # for i j
            cur.append(candidates[i])
            dfs(i,total+candidates[i])
            cur.pop()
            dfs(i+1,total)

        dfs(0,0)
        return res