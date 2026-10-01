# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode | None) -> list[float]:
        if root is None:
            return []

        queue = deque([root])
        list=[]

        while len(queue) > 0:

            level_size=len(queue)

            levelSum=0

            for i in range(len(queue)):
                node = queue.popleft()
                levelSum+=node.val

                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
                            
            average = levelSum/level_size
            list.append(average)

        
        return list
        