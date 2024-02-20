class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for i in range(len(s)):
            if stack:
                if stack[-1] == "(" and s[i] == ")":
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])

        return len(stack)