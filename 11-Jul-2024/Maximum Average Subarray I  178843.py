# Problem: Maximum Average Subarray I  - https://leetcode.com/problems/maximum-average-subarray-i/

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l,r = 0,k
        _sum = sum(nums[l:r])
        av = _sum
        n = len(nums)
        while r<n:
            _sum+=nums[r]
            _sum-=nums[l]
            r+=1
            l+=1
            av = max(av,_sum)
        return av/k


    from itertools import accumulate
    from operator import sub

    f = open('user.out', 'w')
    inp = map(loads, stdin)
    for nums in inp:
        k = next(inp)
        sums = [0] + list(accumulate(nums))
        m = max(map(sub, sums[k:], sums)) / k
        print(m, file=f)