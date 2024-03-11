class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        forward_diagonals = set()
        backward_diagoanls = set()
        columns = set()

        ans = []
        cur = [["."]*n for _ in range(n)]

        def backtrack(row):
            if row >= n:
                temp = ["".join(x) for x in cur]
                ans.append(temp)
                return
            
            for col in range(n):
                if col not in columns and col-row not in backward_diagoanls and col+row not in forward_diagonals:
                    cur[row][col] = "Q"
                    columns.add(col)
                    backward_diagoanls.add(col-row)
                    forward_diagonals.add(col+row)

                    backtrack( row+1 )
                    cur[row][col] = "."
                    columns.discard(col)

                    backward_diagoanls.discard(col-row)
                    forward_diagonals.discard(col+row)


        backtrack(0)
        return ans