class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        mid = num/3
        if int(mid) != mid:
            return []
        else:
            return [int(mid-1),int(mid), int(mid+1)]

            

