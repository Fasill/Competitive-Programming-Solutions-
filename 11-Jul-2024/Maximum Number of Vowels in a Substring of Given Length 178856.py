# Problem: Maximum Number of Vowels in a Substring of Given Length - https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowls = {'a', 'e', 'i', 'o', 'u'}
        l = 0
        r = k
        wind = []
        vownl = 0

        for i in range(k):
            wind.append(s[i])
            if s[i] in vowls:
                vownl += 1
        maxVowls = vownl
        while r < len(s):
            if s[r] in vowls:
                vownl += 1
            if s[l] in vowls:
                vownl -= 1
            l+=1
            r+=1
            maxVowls = max(vownl, maxVowls)
        return maxVowls