class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
            s = len(word1+word2)
            w1 = len(word1)
            w2 = len(word2)
            ans  = ''
            for i in range(s):
                if i <= w1 -1:
                    ans+=word1[i]
                if i <= w2 - 1:
                    ans += word2[i]
            return(ans)


        