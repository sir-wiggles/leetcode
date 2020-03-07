# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return f'{self.val}'

class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if root1 is root2:
            return True

        if root1 is None or root2 is None:
            return False

        if root1.val != root2.val:
            return False

        return (
            self.flipEquiv(root1.left, root2.left) and
            self.flipEquiv(root1.right, root2.right) or
            self.flipEquiv(root1.left, root2.right) and
            self.flipEquiv(root1.right, root2.left) 
        )




null = None
#         |      |                 |                                           |
root1 = [1, 2, 3,    4, 5, 6, null, null, null,    7,    8, null, null]
root2 = [1, 3, 2, null, 6, 4,    5, null, null, null, null,    8,    7]

root1nodes = [TreeNode(n) for n in root1]
root2nodes = [TreeNode(n) for n in root2]

for nodes in [root1nodes, root2nodes]:
    for i, node in enumerate(nodes):
        l = 2*i + 1
        r = 2*i + 2
        if l < len(nodes) and nodes[l].val:
            node.left  = nodes[l]
        if r < len(nodes) and nodes[r].val:
            node.right = nodes[r]

r1 = root1nodes[0]
r2 = root2nodes[0]

print(Solution().flipEquiv(r1, r2))
