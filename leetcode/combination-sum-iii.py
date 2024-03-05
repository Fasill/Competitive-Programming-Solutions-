class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        combs = []
        cur = []
        
        def dfs(i=1,_sum = 0,h=0):
            if _sum == n and len(cur) == k:

                combs.append(cur[:])
                return
        
            if  h >= n or _sum>n or  len(cur) > k or i>9:
                return

            cur.append(i)
            dfs(i+1, _sum+i, h+1)
            cur.pop()
            dfs(i+1, _sum, h)
        dfs()
        return combs