# Problem: Shortest Bridge - https://leetcode.com/problems/shortest-bridge/

from collections import deque

class Solution:
    def isBound(self, i, j):
        return i > -1 and j > -1 and i < self.n and j < self.m
    
    def flipNumber(self, i, j):
        self.grid[i][j] = -1
        for (x, y) in self.dirs:
            dx, dy = i + x, j + y
            if self.isBound(dx, dy) and self.grid[dx][dy] == 1:
                self.flipNumber(dx, dy)
    
    def shortestBridge(self, grid):
        if not grid:
            return None
            
        self.grid = grid    
        self.n, self.m = len(grid), len(grid[0])
        self.dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        found = False
        queue = deque()

        for i in range(self.n):
            for j in range(self.m):
                if self.grid[i][j] == 1:
                    self.flipNumber(i, j)  
                    found = True
                    break
            if found:
                break
        
        for i in range(self.n):
            for j in range(self.m):
                if self.grid[i][j] == -1:
                    for (x, y) in self.dirs:
                        dx, dy = i + x, j + y
                        if self.isBound(dx, dy) and self.grid[dx][dy] == 0:
                            queue.append((i, j, 0))  

        while queue:
            i, j, steps = queue.popleft()

            for x, y in self.dirs:
                dx, dy = i + x, j + y

                if self.isBound(dx, dy):
                    if self.grid[dx][dy] == 1:
                        return steps
                
                    if self.grid[dx][dy] == 0:
                        self.grid[dx][dy] = -1
                        queue.append((dx, dy, steps+1))
        
        return -1