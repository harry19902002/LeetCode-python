# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val>q.val:
            p,q=q,p
        while(q.val<root.val or p.val>root.val):
            root=root.left if q.val<root.val else root.right
        return root