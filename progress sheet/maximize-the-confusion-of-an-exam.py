class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        d = {"F":0,"T":0}

        l = 0
        maxFreq = 0
        maxLeng = 0
        n = len(answerKey)

        for r in range(n):

            d[answerKey[r]] += 1
            maxFreq = max(maxFreq,d[answerKey[r]])
            while (r-l+1)-maxFreq>k:
                d[answerKey[l]] -= 1
                l+=1
            maxLeng = max(r-l+1,maxLeng)


        return maxLeng
