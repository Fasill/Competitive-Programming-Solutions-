# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        _maxDepth = 0
        li = []
        def depthCounter(_maxDepth,node):
            if node:
                _maxDepth += 1
                depthCounter(_maxDepth,node.left)
                depthCounter(_maxDepth,node.right)
            else:
                li.append(_maxDepth)
                _maxDepth-=1
        depthCounter(_maxDepth,root)
        return max(li)