class Solution:
    def maxScore(self, s: str) -> int:
        ones = s.count("1")
        zeros = 0
        running = 0

        for i in range(len(s)-1):
            if s[i] == "0":
                zeros += 1
            else:ones -= 1
            running = max(ones+zeros,running)
        return running