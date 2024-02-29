# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def search(self,node,val):
        stack = []
        def dfs(node,val):

            if not node:
                return
                
            stack.append(node)
            if node.val == val:
                return stack

            left =  dfs(node.left,val)

            if left:
                return left

            right = dfs(node.right,val)
            if right:
                return right

            stack.pop()
            return None
        return dfs(node,val)


    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        first = set(self.search(root,p.val))
        for i in self.search(root,q.val)[::-1]:
            if i in first:
                return i