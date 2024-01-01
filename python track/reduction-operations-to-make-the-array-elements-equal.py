
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        # time complexity O(nlogn)
        def summationn(n):
            return (n*(n+1))//2

        if len(set(nums)) == len(nums):
            return summationn(len(nums)-1)

        elif  len(set(nums)) > 1:
            d = Counter(nums)
           
            d = dict(sorted(d.items(), key=lambda x: x[0], reverse=True))

            s = 0
            c = len(set(nums))-1
            for i in d:
                s+=(d[i]*c)
                c-=1
            return s

        else: return 0

           

            