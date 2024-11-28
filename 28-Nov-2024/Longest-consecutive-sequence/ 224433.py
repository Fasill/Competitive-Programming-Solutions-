# Problem: Longest-consecutive-sequence/ - https://leetcode.com/problems/longest-consecutive-sequence/

from collections import defaultdict
from typing import List

class DSU:
    def __init__(self, nums):
        self.parent = {}
        self.size = {}
        for num in nums:
            self.parent[num] = num
            self.size[num] = 1

    def find(self, n):
        if n != self.parent[n]:
            self.parent[n] = self.find(self.parent[n]) 
        return self.parent[n]

    def union(self, x, y):
        refx = self.find(x)
        refy = self.find(y)
        if refx == refy:
            return
        if self.size[refx] >= self.size[refy]: 
            self.parent[refy] = refx
            self.size[refx] += self.size[refy]
        else:
            self.parent[refx] = refy
            self.size[refy] += self.size[refx]

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dsu = DSU(nums)
        numSet = set(nums)

        for num in nums:
            if num - 1 in numSet:
                dsu.union(num, num - 1)
            if num + 1 in numSet:
                dsu.union(num, num + 1)

        return max(dsu.size.values())
