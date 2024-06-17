# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        p1 = 0
        p2 = int(sqrt(c))
        while p1<=p2:
            if (p1**2)+(p2**2)>c:

                p2 -= 1
            elif (p1**2)+(p2**2)<c:

                p1 += 1
            elif (p1**2)+(p2**2) == c:
                return True
        else:return False
