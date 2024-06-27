# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.traverse_path = []

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root:
            self.traverse_path.append(root.val)
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)
        return self.traverse_path
