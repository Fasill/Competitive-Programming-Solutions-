# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        counter = defaultdict(int)
        def traverce(node):
            if node:
                counter[node.val] += 1
                traverce(node.left)
                
                traverce(node.right)
        traverce(root)
        print(counter)
        _max = 0
        for i in counter:
            _max = max(_max,counter[i])

        li = []
        for i in counter:
            if counter[i] == _max:
                li.append(i)

        return  li

