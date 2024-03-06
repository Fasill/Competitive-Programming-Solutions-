class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left,right = max(weights),sum(weights)

        while left <= right:
            mid = left + (right-left) // 2

            c = 0
            d = 1
            for i in range(len(weights)):
                c += weights[i]
                if c > mid:
                    c = weights[i]
                    d += 1
            
            if d > days:
                left = mid + 1
            else:
                right = mid - 1
        return left

