
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        diff = float('inf')
        _dict = defaultdict(int)

        for i in range(n-2):
            left, right = i+1, n-1

            while left < right:
                _sum = nums[i] + nums[left] + nums[right]
                d = abs(target - _sum)

                if d < abs(diff):
                    diff = target-_sum
                    _dict[diff] = _sum

                if _sum < target:
                    left += 1
                else:
                    right -= 1

        return _dict[diff]
