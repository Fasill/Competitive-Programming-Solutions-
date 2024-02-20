class Solution:
    def numRabbits(self, nums: List[int]) -> int:
        d = defaultdict(int)
        n = len(nums)
        c = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                c += 1
            else:
                if d[nums[i]] > 0:
                    d[nums[i]] -= 1
                else:
                    c+=nums[i]+1
                    d[nums[i]] += nums[i]
        return c

