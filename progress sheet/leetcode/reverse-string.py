class Solution:
    def recursive(self,l,r,s) :
        if l>=r:
            return
        s[l],s[r] = s[r],s[l]
        return self.recursive(l+1,r-1,s)
    def reverseString(self, s: List[str]) -> None:
        l = 0
        r = len(s)-1

        self.recursive(l,r,s)

