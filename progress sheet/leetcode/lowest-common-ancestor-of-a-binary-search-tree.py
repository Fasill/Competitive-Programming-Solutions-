# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        li = []
        def ancestor(node1,p,q):
            if p.val == node1.val:
                li.append(p.val)
                return
            if q.val == node1.val:
                li.append(q.val)
                return
            if  p.val < node1.val and q.val > node1.val:
                li.append( node1.val)
                
                return 
            li.append( node1.val)
            
            if p.val < node1.val and q.val < node1.val:
                return ancestor(node1.left,p,q)
                            
            if p.val > node1.val and q.val > node1.val:
                return ancestor(node1.right,p,q)

        ancestor(root,p,q)
        return TreeNode(li[-1])
        