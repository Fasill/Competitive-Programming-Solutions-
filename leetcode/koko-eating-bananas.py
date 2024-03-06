class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1,max(piles)
        
        while l <= r:

            mid = l +(r-l) // 2
            hr = 0

            for i in range(len(piles)):
                hr += ceil( piles[i]/mid )

            if hr > h:
                l = mid + 1
            else:
                r = mid -1

        return l