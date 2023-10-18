#145. Binary Tree Postorder Traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l=[]
        def postorder(root):
            if root==None:
                return 
            else:
                postorder(root.left)
                postorder(root.right)
                l.append(root.val)
            return l 
        return postorder(root)  
        