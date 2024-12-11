# Problem: Lemonade Change - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        d = defaultdict(int)
        for i in range(len(bills)):
            if bills[i] == 5:
                d[bills[i]] +=1
            else:
                if d[5] == 0:

                    return False
                if bills[i] == 10:
                    d[5]-=1
                    d[10] += 1
                else:
                    if d[10] >0:
                        d[10]-=1
                        d[5] -= 1
                    else:
                        if d[5]>2:
                            d[5]-=3
                        else:
                            return False
        return True
                    