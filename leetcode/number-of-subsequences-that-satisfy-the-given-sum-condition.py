class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = 0
        nums.sort()
        for i in range(n):
            maxi = target-nums[i]
            br = bisect_right(nums,maxi)
            if br>i:
                leng = br-i
                ans += (2**(leng-1))
                # print(br,i,leng,maxi,ans)
        return ans%((10**9) + 7)