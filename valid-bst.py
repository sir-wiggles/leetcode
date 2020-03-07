class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def search(node):
            if not node:
                return True

            lvalid = ((node.left and node.val > node.left.val) or (node.left is None))
            rvalid = ((node.right and node.val < node.right.val) or (node.right is None))
            if not (lvalid and rvalid):
                return False
            return search(node.left) and search(node.right)
        return search(root)
