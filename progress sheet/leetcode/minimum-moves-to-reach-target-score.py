class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        if target == 1:
            return 0
        if maxDoubles == 0:
            return target-1


        n = target
        d = maxDoubles
        c = 0
        while n>0 and d > 0:
            if n%2 == 0:

                n = n//2
                d -= 1
            else:
                n -= 1
            c += 1
        return c + (n-1)

