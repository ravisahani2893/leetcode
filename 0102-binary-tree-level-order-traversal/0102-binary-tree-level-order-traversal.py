# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []
        
        queue = deque([root])
        list=[]
        
        while len(queue) > 0:
        
        
            level_node=[]
        
            for i in range(len(queue)):
                node = queue.popleft()
                level_node.append(node.val)
        
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
                                        
            list.append(level_node)
            
                
        return list
        