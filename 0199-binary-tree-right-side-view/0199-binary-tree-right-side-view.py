# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if root is None:
            return []

        queue=deque([])
        
        
        queue.append(root)

        list=[]

        while(len(queue) > 0):

            levelSize = len(queue)
          
            for i in range(levelSize):
                node = queue.popleft()

                if node.left is not None:
                    queue.append(node.left)
                
                if node.right is not None:
                    queue.append(node.right)
                
                if i == levelSize-1:
                    list.append(node.val)


        return list
        