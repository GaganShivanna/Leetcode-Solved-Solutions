# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def Postorder(root):
            if not root:
                return
            Postorder(root.left)
            Postorder(root.right)
            res.append(root.val)
        Postorder(root)
        return res