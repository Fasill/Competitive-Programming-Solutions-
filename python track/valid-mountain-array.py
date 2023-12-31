class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) <= 2:
            return False

        for i in range(1,len(arr)):
            if arr[i-1]>arr[i]:
                print(arr[:i] ,arr[i:])
                if arr[:i] != sorted(list(set(arr[:i]))) or len(arr[:i]) == 1:
                    return False
                if arr[i:] != sorted(list(set(arr[i:])))[::-1]:
                    return False
                return True
                
                