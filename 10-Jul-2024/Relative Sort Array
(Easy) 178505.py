# Problem: Relative Sort Array
(Easy) - https://leetcode.com/problems/relative-sort-array/

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counter = {}
        for num in arr2:
            counter[num] = []
        ref = []
        for num in arr1:
            if num in counter:
                counter[num].append(num)
            else:
                ref.append(num)
        ref.sort()
        res = []
        for num in arr2:
            res += counter[num]
        res += ref
        return res
