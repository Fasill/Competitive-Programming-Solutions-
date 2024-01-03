class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_dict= {}

        for i ,num in enumerate(numbers):
            t = target-num
            if t in num_dict:
                return [num_dict[t]+1,i+1]
            num_dict[num] = i