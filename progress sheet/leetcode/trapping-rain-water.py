class Solution:
    def trap(self, height: List[int]) -> int:
            if not height:
                return 0

         
            l, r = 0, len(height) - 1
            ans = 0
            max_l = height[l]
            max_r = height[r]
            while l < r:
                if max_l <= max_r:
                    if max_l - height[l] > 0:
                        ans += max_l - height[l]
                    l += 1
                else:
                    if max_r - height[r] > 0:
                        ans += max_r - height[r]
                    r -= 1

                if max_l < height[l]:
                    max_l = height[l]
                if max_r < height[r]:
                    max_r = height[r]
            return ans
