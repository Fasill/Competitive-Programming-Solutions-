class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        n = len(costs)
        ni = 0
        for i in costs:
            if coins-i>=0:
                coins -= i
                ni+=1
            else: return ni
        return n