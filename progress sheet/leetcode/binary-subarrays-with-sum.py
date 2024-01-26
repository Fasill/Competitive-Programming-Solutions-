class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        pref = defaultdict(int)
        pref[0] = 1
        running = 0
        count = 0
        for i in range(len(nums)):
            running += nums[i]
            diff = running - goal
            if diff in pref :
                count += pref[diff]
            pref[running] += 1

        return count        
