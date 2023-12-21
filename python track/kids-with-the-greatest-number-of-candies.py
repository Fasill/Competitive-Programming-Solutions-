class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatestNumbet = max(candies)
        b = []
        for i in candies:
            if i+extraCandies>=greatestNumbet:
                b.append(True)
            else:b.append(False)
        return b