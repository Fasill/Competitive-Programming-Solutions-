# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        li =[]
        def search(node):
            if node:
                li.append(node.val)
                search(node.left)
                search(node.right)
        search(root)

        _sum = 0
        for i in li:
            if i >= low and  i <= high:
                _sum += i
        return _sum