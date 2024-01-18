class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        leng = len(cardPoints)
        l,r = 0,leng-k

        maxPt = 0
        windSum = sum(cardPoints[:r])
        totalPt = sum(cardPoints)

        while r<leng:
            maxPt = max(maxPt,totalPt-windSum)

            windSum += cardPoints[r]
            windSum -=  cardPoints[l]

            l+=1
            r+=1
            
        maxPt = max(maxPt,totalPt-windSum)

        return maxPt
