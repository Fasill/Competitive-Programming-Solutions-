class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        ans = []
        xs = sorted([i[0] for i in intervals ])
        ys = sorted([i[1] for i in intervals ])
        d= {}
        c = 0
        for i in intervals:
            d[i[0]] = c
            c += 1
        for x,y in intervals:
            br = bisect_right(xs,y) 
  
            # print(br)
            if xs[br-1] == y:
                ans.append(d[xs[br-1]])
            else:
                if  br>len(xs)-1:
                    ans.append(-1) 
                else:
                    ans.append(d[xs[br]])
        # print(d)
        return ans
