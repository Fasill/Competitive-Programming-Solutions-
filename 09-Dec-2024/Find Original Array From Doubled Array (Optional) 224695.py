# Problem: Find Original Array From Doubled Array (Optional) - https://leetcode.com/problems/find-original-array-from-doubled-array/

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        counter = collections.Counter(changed)
        res = []
        for k in counter.keys():
            
            if k == 0:
                if counter[k] % 2 > 0:
                    return []
                res += [0] * (counter[k] // 2)
                
            elif counter[k] > 0:
                x = k
                
                while x % 2 == 0 and x // 2 in counter:
                    x = x // 2
                    
                
                while x in counter:
                    if counter[x] > 0:
                        res += [x] * counter[x]
                        if counter[x+x] < counter[x]:
                            return []
                        counter[x+x] -= counter[x]
                        counter[x] = 0
                    x += x
        return res