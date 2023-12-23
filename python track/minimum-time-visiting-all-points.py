class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        tt = 0
    
        for i in range(len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i + 1]
            
            tx = abs(x2 - x1)
            ty = abs(y2 - y1)
            
            tt += max(tx, ty)
        
        return tt