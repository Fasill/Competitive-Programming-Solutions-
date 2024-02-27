class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        res = [1]
        last = self.getRow(rowIndex-1)
        for i in range(1,len(last)):
            res.append(last[i-1]+last[i])
        res.append(1)
        return res
        