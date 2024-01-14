class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:

        l,r = arr.index(max(arr))+1,len(arr)-1
        ans = []
        while 0<=r:
            if arr[:r+1]:
                l = arr.index(max(arr[:r+1]))
                if l == r:
                    r-=1
                    print("s")
                else:
                    arr[:l+1] = arr[:l+1][::-1]
                    ans.append(l+1)
                    arr[:r+1] = arr[:r+1][::-1]
                    ans.append(r+1)
                    r-=1

            else:r-=1
        return ans

            


