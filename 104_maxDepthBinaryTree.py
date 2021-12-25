# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        
        left, right = 0, 0
        if root.left:
            left = self.maxDepth(root.left) + 1
        if root.right:
            right = self.maxDepth(root.right) + 1

        depth = max(left, right, 1)
        return depth
