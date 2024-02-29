# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        li = []
        def inorder(node,i):
            if node:
                li.append((i[0],i[-1],node.val))
                inorder(node.left,(i[0]+1,i[-1]-1))
                inorder(node.right,(i[0]+1,i[-1]+1))
                # d[i[-1]].add((i[0],node.val))
                
        inorder(root,(0,0))
        sortedByCol = sorted(li,key = lambda x:(x[1],x[0],x[2]))
        d = defaultdict(list)
        for i in sortedByCol:
            d[i[1]].append(i[-1])
        res = []
        for i in d:
            res.append(d[i])
        return res
        
