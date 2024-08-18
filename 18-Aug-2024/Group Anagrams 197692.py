# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for i in strs:
            s = "".join(sorted(i))
            d[s].append(i)
        li = []
        for i in d:
            li.append(d[i])
        return li