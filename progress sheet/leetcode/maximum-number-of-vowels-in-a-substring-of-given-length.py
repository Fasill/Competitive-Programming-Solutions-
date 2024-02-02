class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowles ={'a', 'e', 'i', 'o', 'u'}
        l,r =0,0
        n = len(s)
        vowelCounter = 0
        maxVowel = 0
        for i in range(k):
            if s[r] in vowles:
                vowelCounter += 1
            r+=1
        maxVowel = vowelCounter
        while r<n:
            if s[r] in vowles:
                vowelCounter += 1
            if s[l] in vowles:
                vowelCounter -= 1

            r += 1
            l += 1
            maxVowel = max (maxVowel,vowelCounter)
        return maxVowel

                

