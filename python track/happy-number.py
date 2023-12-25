class Solution:
    def isHappy(self, n: int) -> bool:

        def slow(n):
            n = list(str(n))
            ans = 0
            for i in n:
                ans += int(i) ** 2
            n = list(str(ans))
            return ans

        x = []
        while True:
            s = slow(n)
            f= slow(slow(n))
            x.append(s)
            if s == 1 or f == 1:
                return True
            elif f in x:
                return False
            n = slow(n)
