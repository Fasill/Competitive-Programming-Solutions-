# Problem: IPO - https://leetcode.com/problems/ipo/

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        N = len(profits)
        capitalHeap = []
        tempHeap = []
        
        for index in range(N):
            heappush(capitalHeap,[capital[ index ], profits[ index ]])
        
        for _ in range(k):

            while capitalHeap:
                cur = heappop(capitalHeap)
                if cur[0] > w:
                    heappush(capitalHeap, cur )
                    break
                
                else:
                    heappush(tempHeap, -cur[1] )

            if tempHeap:
                cur = heappop(tempHeap)
                w += (-cur)
        return w