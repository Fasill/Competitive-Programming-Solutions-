# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        li = []
        def inorder(node):
            if node:
                inorder(node.left)
                li.append(node.val)
                inorder(node.right)
            
        inorder(root)
        # print(li)
        for i in range(1,len(li)):
            if li[i-1] >= li[i]:
                return False
        return True