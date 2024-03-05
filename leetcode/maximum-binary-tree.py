# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def DnQ(nums):
            
            if len(nums) == 1:
                return TreeNode(nums[0])
            if not nums:
                return
            maxNum = max(nums)
            root = TreeNode(maxNum)
            i = nums.index(maxNum)
            root.left = DnQ(nums[:i])
            root.right = DnQ(nums[i+1:])

            return root
        return DnQ(nums)
