class Solution:
    def maxScore(self, s: str) -> int:
        maxScore = 0
        for i in range(1,len(s)):
            zeros = s[:i].count("0")
            ones = s[i:].count("1")
            maxScore = max(maxScore,zeros+ones)
        return maxScore
        