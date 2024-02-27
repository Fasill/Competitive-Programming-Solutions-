class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n<0:
            n = abs(n)
            x = 1/x
        last = self.myPow(x,n//2)
        if n%2:
            return last*last*x
        else:
            return last*last
