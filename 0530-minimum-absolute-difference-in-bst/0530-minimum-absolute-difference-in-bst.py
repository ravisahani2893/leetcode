# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        list=[]
       
        def minimumDiff(list, root):
            
            if root is None:
                return

            
            minimumDiff(list,root.left)
            list.append(root.val)
            minimumDiff(list,root.right)
            
            
            return list
                    
        
        
        inorderList= minimumDiff(list, root)

        prev=inorderList[0]
        minimum=float('inf')
        for i in range(1,len(inorderList)):
            minimum=min(minimum, inorderList[i]-prev)
            prev=inorderList[i]


        return minimum
        