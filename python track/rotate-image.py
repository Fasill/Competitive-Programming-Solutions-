class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # time complexity O(m*n^2)
        li = []
        q = matrix.copy()
        for i in range(len(matrix[0])):
            row = []
            for j in q:
                row.append(j[i])
            matrix[i] = row[::-1]
       
                
        