class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        l,r = 0,len(mat[0])-1
        s = 0
        for i in range(len(mat)):
            if l == r:
                s += mat[i][l]
            else:
                s += mat[i][l]+mat[i][r]
            l+=1
            r-=1
        return s