class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        prifix = []
        for i in range(len(matrix)+1):
            li =[] 
            for j in range(len(matrix[0])+1):
                li.append(0)
            prifix.append(li)
        for i in range(1,len(matrix)+1):
            for j in range(1,len(matrix[0])+1):
                prifix[i][j] = matrix[i-1][j-1]+ prifix[i-1][j]+prifix[i][j-1]-prifix[i-1][j-1]

        self.prifix = prifix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
            prifix = self.prifix
           

            return ((prifix[row2+1][col2+1]-prifix[row1][col2+1]) -prifix[row2+1][col1])+prifix[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)