class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        
        res = []
        s = list(s)
        c = 0
        for i in range(0,len(s),k):
            temp = list(s[i:min(i+k,len(s))])
            if c %2 == 0:
                temp.reverse()

            res += temp
            c+=1
        return "".join(res)