class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def calc(p):
            return sqrt(((0-p[0])**2)+((0-p[-1])**2))
        x = []
        for i in points:
            c = calc(i)
            i.append(c)
            x.append(i)
        x = sorted(x,key=lambda x:x[2],reverse = True)
        print(x)
        ans = []

        for i in range(k):
            ans.append(x.pop()[:2])
        return ans
            