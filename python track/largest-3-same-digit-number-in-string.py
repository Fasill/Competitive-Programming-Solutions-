class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n = len(num)
        max_good = ""

        for i in range(n - 2):
            substring = num[i:i + 3]
            if len(set(substring)) == 1: 
                if substring > max_good:
                    max_good = substring

        return max_good
