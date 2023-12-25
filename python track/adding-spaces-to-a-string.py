class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = ""
        l = 0
        for i in spaces:
            res += s[l:i]
            res += " "
            l = i
        res += s[l:]
        return(res)