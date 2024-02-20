class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(set(s)) == 1:
            return len(s)
        d = Counter(s)
        o = 0
        z = False
        
        for i in d:
            if d[i] == 1 :
                if z:
                    o+=1
                z = True
                
            elif d[i]%2 != 0 :
                if z:
                    o += 1
                z = True
        return len(s)-o

            