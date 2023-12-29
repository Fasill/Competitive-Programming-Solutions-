class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        t = set(fronts).union(set(backs))
        
        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                t.discard(fronts[i])

        j = list(t)

 
        return min(j) if j else 0
        

