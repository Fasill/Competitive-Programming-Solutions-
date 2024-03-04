class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = [[]]
        cur = []
        n = len(nums)

        def track(i):
            if i == n:
                # subset.append(cur[:])
                return

            for j in range(i,n):
                cur.append(nums[j])
                subset.append(cur[:])

                track(j+1)
                cur.pop()
        track(0)
        return subset