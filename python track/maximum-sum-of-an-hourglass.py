class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        li = []
        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                c = 0
                c += sum(grid[i][j:j + 3])
                c += grid[i + 1][j + 1]
                c += sum(grid[i + 2][j:j + 3])

                
                li.append(c)

        return max(li)