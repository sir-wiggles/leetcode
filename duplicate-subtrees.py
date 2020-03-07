from collections import defaultdict, Counter


class Solution(object):
    def findDuplicateSubtrees(self, root):
        trees = defaultdict()
        trees.default_factory = trees.__len__
        count = Counter()
        ans = []
        def lookup(node):
            if node:
                uid = trees[node.val, lookup(node.left), lookup(node.right)]
                count[uid] += 1
                if count[uid] == 2:
                    ans.append(node)
                return uid

        lookup(root)
        return ans
