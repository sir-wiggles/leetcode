# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)

class Solution:        

    def swapPairs(self, head: ListNode, index: int = 0) -> ListNode:
        if not head or not head.next:
            return head
        # A -> B -> C -> ...
        a = head 
        b = a.next
        # B -> A    C -> ... 
        #      |
        #      +--> D -> C -> E
        a.next = self.swapPairs(b.next)
        b.next = a
        return b

    def swapPairs2(self, head: ListNode) -> ListNode: 

        dummy = ListNode(-1)
        dummy.next = head

        prev = dummy
        while head and head.next:

            a = head 
            b = a.next

            prev.next = b
            a.next = b.next
            b.next = a

            prev = a
            head = a.next

        return dummy.next


nodes = []
for v in [1, 2, 3, 4]:
    nodes.append(ListNode(v))

for i, n in enumerate(nodes[:-1], start=1):
    n.next = nodes[i]

node = Solution().swapPairs2(nodes[0])
while node:
    print(node)
    node = node.next
