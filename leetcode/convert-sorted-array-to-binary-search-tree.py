# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 1:
            return TreeNode(nums[0])
        if len(nums) == 0:
            return
        
        cur = len(nums)//2
        node = TreeNode(nums[cur])
        left = self.sortedArrayToBST(nums[:cur])
        right = self.sortedArrayToBST(nums[cur+1:])
        
        node.left = left
        node.right = right
        return node
