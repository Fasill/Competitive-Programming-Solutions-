class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        les = []
        great = []
        mid = []
        for i in nums:
            if i > pivot:
                great.append(i)
            elif i<pivot:
                les.append(i)
            else:
                mid.append(i)
        return [*les,*mid,*great]