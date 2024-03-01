class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        refunds = []
        maxCost = 0
        for a, b  in costs:
            refunds.append(b - a)
            maxCost += a
        refunds.sort()

        return maxCost+sum(refunds[:len(refunds)//2])