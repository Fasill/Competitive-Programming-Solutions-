# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        result = []
        def calculator(node,val):
            if not node :
                return node
            if not node.left and not node.right:
                result.append(val+node.val)

            val = val+node.val
            # node.val = val
            calculator(node.left,val*10)
            calculator(node.right,val*10)
        calculator(root,0)
        print(result)
        return sum(result)
            



