class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        nums = nums[::-1]
        prev = float("-inf")
        stack = []
        for num in nums:
            while stack and stack[-1] < num:
                prev = max(prev, stack.pop())
            else:
                if num < prev:
                    return True

            stack.append(num)
        return False        
                