
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)

class Solution:

    def findMid(self, head: ListNode) -> ListNode:
        slow = head.next
        fast = head.next.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if fast:
            return slow.next
        return slow

    def reverse(self, head: ListNode) -> ListNode:
        prev = None
        while head:
            temp = head
            head = head.next
            temp.next = prev
            prev = temp
        return prev

    def isPalindrome(self, head: ListNode) -> bool:

        if head is None:
            return False
        if head.next is None:
            return True

        mid = self.findMid(head)
        rev = self.reverse(mid)

        while rev:
            if rev.val != head.val:
                return False
            rev = rev.next
            head = head.next
        return True

head = ListNode(1)
#  head.next = ListNode(2)
#  head.next.next = ListNode(2)
#  head.next.next.next = ListNode(1)

#  head = ListNode(1)
#  head.next = ListNode(2)
#  head.next.next = ListNode(3)
#  head.next.next.next = ListNode(2)
#  head.next.next.next.next = ListNode(1)

#  head = ListNode(1)
#  head.next = ListNode(2)
#  head.next.next = ListNode(3)
#  head.next.next.next = ListNode(4)
#  head.next.next.next.next = ListNode(5)

head = Solution().isPalindrome(head)
print(head)

#  while head:
    #  print(head)
    #  head = head.next
