class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        x = set(arr)
        for i in x:
            if (arr.count(i)/len(arr))*100>25:
                return i
            
        