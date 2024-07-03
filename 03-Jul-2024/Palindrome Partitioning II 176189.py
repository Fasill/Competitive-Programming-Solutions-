# Problem: Palindrome Partitioning II - https://leetcode.com/problems/palindrome-partitioning-ii/

class Solution:
    def minCut(self, S):
        N = len(S)
        dp = [-1] + [N] * N
        for i in range(2 * N - 1):
            l = i // 2
            r = l + (i & 1)
            while 0 <= l and r < N and S[l] == S[r]:
                dp[r + 1] = min(dp[r + 1], dp[l] + 1)
                l -= 1
                r += 1
        return dp[-1]