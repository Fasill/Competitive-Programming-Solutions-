class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minQue = deque([])
        maxQue = deque([])
        start = end = maxLeng = 0
        n = len(nums)

        while end<n:
            
            while minQue and minQue[-1] > nums[end]:
                minQue.pop()
            minQue.append(nums[end])

            while maxQue and maxQue[-1] <nums[end]:
                maxQue.pop()
            maxQue.append(nums[end])

            while maxQue[0]-minQue[0]>limit:
                num = nums[start]
                if num == maxQue[0]:
                    maxQue.popleft()
                if num == minQue[0]:
                    minQue.popleft()
                start += 1
            maxLeng = max(maxLeng,end-start+1)
            end+=1
        return maxLeng