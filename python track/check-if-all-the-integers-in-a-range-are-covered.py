class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        x = [i for i in range(left,right+1)]

        for i in ranges:
            for j in range(i[0],i[1]+1):
                if j in x:
                    x.remove(j)
                
        if len(x) == 0:
            return True
        return False