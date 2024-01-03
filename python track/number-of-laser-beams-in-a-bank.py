class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        li = []
        for i in bank:
            n = i.count("1")
            if n!=0:
                li.append(n)
        if li:
            ans = 0
            for i in range(1,len(li)):
                ans+=(li[i-1]*li[i])
            return ans
        else:
            return 0