class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        r1 = set("qwertyuiop")
        r2 = set("asdfghjkl")
        r3 = set("zxcvbnm")
        ans = []

        for i in words:
            x = set(i.lower())  
            if x <= r1 or x <= r2 or x <= r3:
                ans.append(i)

        return ans
