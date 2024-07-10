# Problem: Minimum Common Value - https://leetcode.com/problems/minimum-common-value/

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        pointer_1 = 0
        pointer_2 = 0

        while pointer_1 < len(nums1) and pointer_2 < len(nums2):
            if nums1[pointer_1] == nums2[pointer_2]:
                return nums1[pointer_1]
            elif nums1[pointer_1] > nums2[pointer_2]:
                pointer_2 +=1
            else:
                pointer_1 +=1

        return -1