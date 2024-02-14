class Solution:
    def minimumSteps(self, s: str) -> int:
        z= s.count("0")
        c = 0
        for char in s:
            if char == "0":
                z-=1
            else:
                c+=z
        return c