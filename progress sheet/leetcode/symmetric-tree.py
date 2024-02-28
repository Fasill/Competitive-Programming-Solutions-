# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def mirror(leftNode,rightNode):
            if not leftNode or not rightNode:
                if not leftNode and not rightNode:
                    return True
                return False

            if leftNode.val != rightNode.val:
                return False
            return mirror(leftNode.right,rightNode.left) and mirror(leftNode.left,rightNode.right)

        return mirror(root.left,root.right)