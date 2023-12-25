class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p = []
        n = []
        for i in nums:
            if i>0:
                p.append(i)
            else:
                n.append(i)
        x = 1
        ans = []
        for i in range(max(len(p),len(n))):
            ans.append(p[i])
            ans.append(n[i])


        return ans
