from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        return str(self.val)

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        slow = fast = prev = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None

        l1 = self.sortList(head)
        l2 = self.sortList(slow)

        dummy = tail = ListNode(-1)
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = ListNode(l1.val)
                l1 = l1.next
            else:
                tail.next = ListNode(l2.val)
                l2 = l2.next
            tail = tail.next

        if l1 is None:
            tail.next = l2
        elif l2 is None:
            tail.next = l1

        return dummy.next




import unittest
class Test(unittest.TestCase):

    def buildList(self, i):
        dummy = ListNode(-1)
        curr = dummy
        for n in i:
            curr.next = ListNode(n)
            curr = curr.next
        return dummy.next

    def check(self, head: ListNode, values: List[int]):
        values = sorted(values)
        i = 0
        while head:
            self.assertEqual(head.val, values[i])
            i += 1
            head = head.next
        self.assertEqual(i, len(values))

    def test1(self):
        i = [4, 2, 1, 3]
        root = self.buildList(i)
        root = Solution().sortList(root)
        self.check(root, i)

    def test2(self):
        i = [4, 2, 1]
        root = self.buildList(i)
        root = Solution().sortList(root)
        self.check(root, i)
    
    def test3(self):
        i = [2, 1]
        root = self.buildList(i)
        root = Solution().sortList(root)
        self.check(root, i)

    def test4(self):
        import random
        i = list(range(100))
        random.shuffle(i)
        root = self.buildList(i)
        root = Solution().sortList(root)
        self.check(root, i)



unittest.main(exit=False)
