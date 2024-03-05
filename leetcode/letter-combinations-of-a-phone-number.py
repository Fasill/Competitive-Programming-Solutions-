class Solution:
    def letterCombinations(self, nums: str) -> List[str]:
        di = {
            2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz",
        }
        n = len(nums)
        ans = []
        cur = []
        def track(i,j=0):
            if i == n:
                if cur:
                    ans.append("".join(cur[:]))
                return 
            for k in range(len(di[int(nums[i])])):
                cur.append(di[int(nums[i])][k])
                track(i+1,k+1)
                cur.pop()
                    
            
        track(0)
        
        return ans
