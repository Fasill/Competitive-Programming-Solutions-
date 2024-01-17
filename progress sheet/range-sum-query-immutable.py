class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixes = []
        c = 0
        for i in range(len(nums)):
            c+=nums[i]
            self.prefixes.append(c)
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        prefixes = self.prefixes 
        if left == 0:
            return prefixes[right]
        else:
            return prefixes[right] - prefixes[left-1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)