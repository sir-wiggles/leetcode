from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        def helper(po: List[int], io: List[int]):
            
            if len(po) == 1:
                return TreeNode(io[0])
            elif len(po) == 0:
                return None
            
            root = TreeNode(po[0])
            index = io.index(root.val)

            root.left = helper(po[1:index+1], io[:index])
            root.right = helper(po[index+1:], io[index+1:])
            return root
        
        root = helper(preorder, inorder)
        return root

preorder = [3,9,10,11,12,20,15,7]
inorder = [12,11,10,9,3,15,20,7]

#  preorder = [1, 2, 3, 4, 5]
#  inorder = [1, 2, 3, 4, 5]

#  preorder = [3,9,10,20,15,7]
#  inorder = [9,10,3,15,20,7]


print(Solution().buildTree(preorder, inorder))
