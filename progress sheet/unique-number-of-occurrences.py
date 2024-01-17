class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        x = []
        for i in list(set(arr)):
            x.append(arr.count(i))
        return len(x) == len(set(x))