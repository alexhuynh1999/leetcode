# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
                
        visited = set()
        queue, layers = [(root, 0)], []
        while len(queue) > 0:
            curr_node, level = queue.pop(0)
            
            if level >= len(layers):
                layers.append([])
            layers[level].append(curr_node.val)
                
            if curr_node.left: 
                queue.append((curr_node.left, level + 1))
            if curr_node.right: 
                queue.append((curr_node.right, level + 1))
                        
        return [l[-1] for l in layers]
