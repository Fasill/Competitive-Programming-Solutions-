from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        d = defaultdict(int)
        l = 0
        maxFruit = 0
        lengFruits = len(fruits)

        for r in range(lengFruits):
            d[fruits[r]] += 1
            while len(d) > 2:
                d[fruits[l]] -= 1
                if d[fruits[l]] == 0:
                    del d[fruits[l]]
                l += 1
            maxFruit = max(maxFruit, (r - l) + 1)

        return maxFruit
