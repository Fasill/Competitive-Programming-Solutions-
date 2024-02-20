class Solution:
    def breakPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return ""
        n = len(s)//2
        for i in range(n):
            if s[i] != "a":
                print(s[i])
                s,y = s[:i],s[i+1:]
                s+="a"+y
                break
        if s == s[::-1]:
            s = s[:len(s)-1]
            s+="b"
        return s
            