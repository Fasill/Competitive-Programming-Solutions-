class Solution:
    def reverseString(self, s: List[str]) -> None:
            l,r = 0,len(s)-1
            while r>l:
                s[l],s[r] =s[r],s[l] 
                l+=1
                r-=1
            return s