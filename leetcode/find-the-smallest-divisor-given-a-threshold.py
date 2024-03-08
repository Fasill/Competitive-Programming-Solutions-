class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        l,r = 1,max(nums)
        n = len(nums)
        while l <= r:

            mid = l + (r-l) // 2

            _sum = 0
            for num in nums :
                _sum +=  ceil(num/mid)
            if _sum > threshold:
                l = mid + 1
            else:
                r = mid - 1
        return l
        