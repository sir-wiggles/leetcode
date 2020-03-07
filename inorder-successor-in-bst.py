# Definition for a binary tree node.
#  class TreeNode:
   #  def __init__(self, x):
        #  self.val = x
        #  self.left = None
        #  self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':

        # successor lower in the tree
        if p.right:
            p = p.right
            while p.left:
                p = p.left
            return p

        # successor upper in the tree
        stack = []
        inorder = -float('inf')

        while stack or root:

            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            if p.val == inorder:
                return root
            inorder = root.val
            root = root.right
        return None
        
