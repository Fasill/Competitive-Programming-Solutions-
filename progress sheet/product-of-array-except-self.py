class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeros = 0
        arraLeng = len(nums)
        for num in nums:
            if num == 0:
                zeros+=1
            else:
                product *= num

        result = []

        if zeros>1:
            result = [0]*arraLeng
        elif zeros == 1:
            for num in nums:
                if num == 0:
                    result.append(product)
                else:
                    result.append(0)
        else:
            for num in nums:
                result.append(product//num)
        return result

            