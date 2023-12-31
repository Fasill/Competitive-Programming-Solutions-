class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        d = [str(i) for i in digits]
        _str  = "".join(d)
        return [ int(i) for i in str(int(_str)+1)]

