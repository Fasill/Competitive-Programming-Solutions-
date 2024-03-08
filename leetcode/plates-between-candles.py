class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        li = [0]
        indexes = []
        for i in range(len(s)):
            if s[i] == "*":
                li.append(1)
            else:
                li.append(0)
                indexes.append(i+1)
        
        for i in range(1,len(li)):
            li[i] = li[i-1] + li[i]
        
        ans = []
        for i,j in queries:
            left = bisect_left(indexes,i+1)
            right = bisect_right(indexes,j+1) -1
            if left > right:
                ans.append(0)

            else:            

                ans.append( li[indexes[right]] - li[indexes[left]] )
        print(li,indexes)
        return ans