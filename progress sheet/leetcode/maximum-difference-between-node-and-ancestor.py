# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        stack = []
        self.ans = 0
        l = 0
        def dfs(node):
            if not node:
                return
            if stack:
                for val in stack:
                    self.ans = max(abs(val-node.val),self.ans)

            stack.append(node.val)
            left = dfs(node.left)
            if left:
                return left
            right = dfs(node.right)
            if right:
                return right                
            stack.pop()
            return None

        dfs(root)
        return self.ans