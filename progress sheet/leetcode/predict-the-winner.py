class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        def pridict(l,r,role):
            if l == r:
                if role:
                    return [nums[l],0]
                else:
                    return [0,nums[l]]

            if role:
                left = pridict(l+1,r,not role)
                right = pridict(l,r-1,not role)
                left[0] += nums[l]
                right[0] += nums[r]
                if left[0]>right[0]:
                    return left
                else:
                    return right
            else:
                left = pridict(l+1,r,not role)
                right = pridict(l,r-1,not role)
                left[1] += nums[l]
                right[1] += nums[r]
                if left[1]>right[1]:
                    return left
                else:
                    return right

        p1,p2 = pridict(0,len(nums)-1,True)
        if p1>=p2:
            return True
        return False