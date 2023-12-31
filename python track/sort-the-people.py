class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:       
        d = {}
        for i in range(len(names)):
            d[heights[i]] = names[i]
        return [d[i] for i in sorted(heights)[::-1] ]
     
            
