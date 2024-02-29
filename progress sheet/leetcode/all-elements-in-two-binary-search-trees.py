# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        li = []
        def iterator(node1):
            if not node1 :
                return
            li.append(node1.val)
            iterator(node1.left)
            iterator(node1.right)

        iterator(root1)
        def iterator(node1):
            if not node1 :
                return
            li.append(node1.val)
            iterator(node1.left)
            iterator(node1.right)

        iterator(root2)
        return sorted(li)