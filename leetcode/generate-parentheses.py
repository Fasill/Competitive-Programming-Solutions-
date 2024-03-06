class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        li = ["(",")"]
        cur = []
        res = []
        def backtrack(c1,c2):
            if c1 ==  c2 == n:
                res.append("".join(cur))
                return
            if c1<n:
                cur.append("(")
                backtrack(c1+1,c2)
                cur.pop()
            if c1>c2:
                cur.append(")")
                backtrack(c1,c2+1)
                cur.pop()


        backtrack(0,0)
        print(res)
        return res