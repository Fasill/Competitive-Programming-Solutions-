class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ans = {}

        for i in range(len(list1)):
            if list1[i] in list2:
                x =(i+list2.index(list1[i]))

                if x in ans:
                    ans[x].append(list1[i])
                else:
                    ans[x]=[list1[i]]
        x = min(ans)
        return ans[x]