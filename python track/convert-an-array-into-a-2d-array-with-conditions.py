class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        d = Counter(nums)
        maxv = float("-inf")

        for i in d.values():
            maxv = max(maxv,i)
        ans  =[]
        print(maxv)
        for i in range(maxv):
            temp = []
            for j in d:
                if d[j] >0:
                    temp.append(j)
                    d[j]-=1

            ans.append(temp)
        return ans
            




