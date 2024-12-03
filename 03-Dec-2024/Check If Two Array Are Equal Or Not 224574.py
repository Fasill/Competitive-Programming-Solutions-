# Problem: Check If Two Array Are Equal Or Not - https://practice.geeksforgeeks.org/problems/check-if-two-arrays-are-equal-or-not3847/1?utm_source=geeksforgeeks&utm_medium=article_practice_tab&utm_campaign=article_practice_tab

# User function Template for python3
from collections import Counter
class Solution:
    # Function to check if two arrays are equal or not.
    def check(self, arr1, arr2) -> bool:
        #code here

        ref = Counter(arr1)
        ref2 = Counter(arr2)
        return ref == ref2