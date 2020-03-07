# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        def search(node, lower = -float('inf'), upper = float('inf')):

            if node is None:
                return True

            if lower < node.val < upper:
                return search(node.left, lower, upper=node.val) and search(node.right, lower=node.val, upper)
            else:
                return False

        return search(root)

