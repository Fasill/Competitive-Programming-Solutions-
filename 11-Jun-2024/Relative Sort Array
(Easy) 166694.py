# Problem: Relative Sort Array
(Easy) - https://leetcode.com/problems/relative-sort-array/

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counter = Counter(arr1)
        res = []
        for num in arr2:
            if num in counter:
                while counter[num]:
                    res.append(num)
                    counter[num] -= 1
                    
        cur = []
        for num in counter:
            while counter[num]:
                cur.append(num)
                counter[num] -= 1
        cur.sort()
        return res+cur