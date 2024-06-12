# Problem: Find Center of Star Graph - https://leetcode.com/problems/find-center-of-star-graph/

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        indegrees = defaultdict(int)

        for src,dst in edges:
            indegrees[src] += 1
            indegrees[dst] += 1
        
        _max = max(indegrees.values())
        for i in indegrees:
            if indegrees[i] == _max:
                return i
            