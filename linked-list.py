from typing import List

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0

    def _get(self, index: int) -> List[Node]:

        if self.size == 0:
            return [None, None, None]

        p = None
        c = self.head
        n = c.next

        count = 0
        while count < self.size:
            if count == index:
                return [p, c, n]
            p = c
            c = n
            if n is None:
                break
            n = n.next
            count += 1
        return [p, c, n]

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        p, c, n = self._get(index)
        if c is None:
            return -1
        return c.value

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node = Node(val)
        if self.size == 0:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node = Node(val)
        if self.size == 0:
            self.head = node
        else:
            p, c, n = self._get(-1)
            p.next = node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index == self.size:
            return self.addAtTail(val)
        if index == 0:
            return self.addAtHead(val)
        if index > self.size:
            return

        node = Node(val)
        p, c, n = self._get(index)

        node.next = c
        p.next = node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index >= self.size:
            return

        self.size -= 1
        p, c, n = self._get(index)
        if p is None:
            self.head = n
            return
        p.next = n

# P  C  N
#  [ 0, 1, 2, 3 ]
#    P  C  N

# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
obj.addAtIndex(0, 10)
obj.addAtIndex(1, 20)
obj.addAtIndex(1, 30)
obj.addAtTail(50)
obj.get(0)

node = obj.head
while node is not None:
    print(node)
    node = node.next
