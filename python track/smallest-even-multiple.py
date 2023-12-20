class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
            b = True
            c = n
            if n % 2 == 0:
                return n
            else:
                while b:
                    if n%2 == 0 and n%c == 0:
                        return n
                    n+=1
