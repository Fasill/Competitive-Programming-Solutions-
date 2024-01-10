class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        m = float('-inf')
        l = 0
        vowel = ["a","e","o","i","u"]
        while k<=len(s):
            w = s[l:k]
            totalVowel = 0
            for i in vowel:
                if i in w:
                    totalVowel += w.count(i)
            m = max(m,totalVowel)
            k+=1
            l+=1
        return m