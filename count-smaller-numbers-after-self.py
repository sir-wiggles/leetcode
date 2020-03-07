from typing import List

class SolutionV0:
    def countSmaller(self, nums: List[int]) -> List[int]:

        res = []
        nums.append(-float('inf'))
        for i in range(len(nums)):
            n = nums[i]
            count = 0
            for c in range(i, len(nums)-1):
                if nums[c] < n:
                    count += 1
            res.append(count)
        return res[:-1]

class TreeNode:
    def __init__(self, val: int, eqCount: int=0, lessCount: int=0):
        self.lessCount: int = lessCount
        self.val: int = val
        self.eqCount: int = eqCount
        self.left: TreeNode = None
        self.right: TreeNode = None

def Insert(root: TreeNode, val: int):

    if val == root.val:
        root.eqCount += 1
        return

    if val < root.val:
        root.lessCount += 1
        if root.left is None:
            root.left = TreeNode(val, 1, 0)
        else:
            Insert(root.left, val)
        return

    if root.right is None:
        root.right = TreeNode(val, 1, 0)
    else:
        Insert(root.right, val)

def LessCounter(root: TreeNode, val: int) -> int:
    if root is None:
        return 0

    if val == root.val:
        return root.lessCount

    if val < root.val:
        return LessCounter(root.left, val)

    return root.lessCount + root.eqCount + LessCounter(root.right, val)


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []

        if len(nums) == 1:
            return [0]

        root = TreeNode(nums[-1], 1, 0)

        res = [0] * len(nums)
        i = len(nums) - 2
        while i >= 0:
            n = nums[i]
            Insert(root, n)
            res[i] = LessCounter(root, n)
            i -= 1

        return res




test = [5, 2, 6, 1]
print(Solution().countSmaller(test))
