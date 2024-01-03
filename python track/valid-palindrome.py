class Solution:
    def isPalindrome(self, s: str) -> bool:
            alphanumeric_str = ''.join(c for c in s if c.isalnum()).lower()
            return alphanumeric_str == alphanumeric_str[::-1]