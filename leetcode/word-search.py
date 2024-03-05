class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        COL,ROW,lengthOfWord = len(board[0]),len(board),len(word)
        # COL, ROW, lengthOfWord = len(board), len(board[0]), len(word)

        def isInInterval(r,c):
            if r < 0 or c < 0 or r >= ROW or c >= COL or (r,c) in paths:
                return True
            return False
    

            
        paths = set()
        
        def dfs(r,c,i):
            if i == lengthOfWord:
                return True
            if isInInterval(r,c) or board[r][c] != word[i]:
                return False

            paths.add((r,c))
            res = ( 
                    dfs(r+1,c,i+1) or 
                    dfs(r-1,c,i+1) or 
                    dfs(r,c+1,i+1) or 
                    dfs(r,c-1,i+1)
                    )
            paths.discard((r,c))
            return res

        for r in range(ROW):
            for c in range(COL):
                if dfs(r,c,0):
                    return True
        return False

            