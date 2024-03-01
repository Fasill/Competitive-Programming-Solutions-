# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return 
        node1 = root.left
        node2 = root.right
        d = defaultdict(list) 
        
        def validator(node,x,y):
            if not node:
                return node

            d[y].append(node.val)
            validator(node.left,x-1,y+1)
            validator(node.right,x+1,y+1)
        validator(root,0,0)
        li = []
        bol = True
        for i in d:
            if bol:
                li.append(d[i])
                bol = not bol
            else:
                li.append(d[i][::-1])
                bol = not bol

        return li
