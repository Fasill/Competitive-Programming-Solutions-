class Solution:
    def putMarbles(self, nums: List[int], k: int) -> int:
        sums = []
        for i in range(1,len(nums)):
            sums.append(nums[i]+nums[i-1])
        sums.sort()
        _min = 0
        _max = 0

        j = len(sums)-1
        for i in range(k-1):
            _min += sums[i]
            _max += sums[j]
            j -= 1
        return _max-_min