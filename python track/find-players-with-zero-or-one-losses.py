class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        s = {}

        for i in matches:
            if i[0] in s:
                s[i[0]].append(True)
            else:
                s[i[0]] = [True]
            if i[-1] in s:
                s[i[-1]].append(False)
            else:
                s[i[-1]] = [False]

        l1 = []
        l2 = []
        for i in s:
            if s[i].count(False) == 0:
                l1.append(i)
            elif s[i].count(False) == 1:
                l2.append(i)
        return [sorted(l1),sorted(l2)]