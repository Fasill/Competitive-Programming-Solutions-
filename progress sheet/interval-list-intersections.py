class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        fl = firstList
        sl = secondList
        ans = []
        for i in fl:
            for j in sl:
                if i[0]<=j[1] and j[0]<=i[1]:
                    ans.append([max(i[0],j[0]),min(i[1],j[1])])

        return ans
