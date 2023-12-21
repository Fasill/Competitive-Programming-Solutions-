class Solution:
    def numberOfMatches(self, n: int) -> int:
        if n == 1:
            return 0
        elif n % 2 == 0:
            # Even number of teams
            return n // 2 + self.numberOfMatches(n // 2)
        else:
            # Odd number of teams
            return (n - 1) // 2 + self.numberOfMatches((n - 1) // 2 + 1)
