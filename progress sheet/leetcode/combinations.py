class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def back(i,cur,k):
            if len(cur) == k:
                ans.append(cur[:])
                return
            if i > n:
                return

            cur.append(i)
            back(i+1,cur,k)
            cur.pop() 
            back(i+1,cur,k)

        back(1,[],k)
        return ans
