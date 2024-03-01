class Solution:
    def trap(self, height: List[int]) -> int:

        moStack1 = []
        moStack2 = []

        n = len(height)

        for i in range(n):
            if not moStack1 or moStack1[-1]<height[i]:
                moStack1.append(height[i])
            else:
                moStack1.append(moStack1[-1])
                
            if not moStack2 or moStack2[-1]<height[-(i+1)]:
                moStack2.append(height[-(i+1)])
            else:
                moStack2.append(moStack2[-1])

        moStack2 = moStack2[::-1]   
        ans = 0

        for i in range(n):
            diff = min(moStack2[i],moStack1[i]) - height[i]
            if diff>=0:
                ans += diff

        return ans

            
