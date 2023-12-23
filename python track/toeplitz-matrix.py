class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix[0])):
            val = matrix[0][i]
            t = i
            for j in range(1, len(matrix)):
                t += 1
                if t == len(matrix[0]):
                    break
                if matrix[j][t] != val:
                    return False


        for q in range(1,len(matrix)):
            val = matrix[q][0]
            t = 1
            for h in range(q+1,len(matrix)):
                if t >= len(matrix[0]):
                    break
                if matrix[h][t] != val:

                    return False
                t += 1
        return True