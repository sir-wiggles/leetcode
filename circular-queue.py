class Node:
    def __init__(self, val: int = -1):
        self.val = val
        self.next = None

    def __repr__(self):
        return str(self.val)

class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.capacity = k
        self.size = 0
        head = Node()
        prev = head
        for i in range(1, k):
            curr = Node(-1)
            prev.next = curr
            prev = curr
        prev.next = head

        self.head = head
        self.tail = head

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        if self.isEmpty():
            self.head = self.head.next
        self.tail = self.tail.next
        self.tail.val = value
        self.size += 1
        return True


    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.head.val = -1
        self.head = self.head.next
        self.size -= 1
        if self.isEmpty():
            self.tail = self.tail.next
        return True


    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        return self.head.val


    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        return self.tail.val


    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.size == 0


    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.size == self.capacity

["MyCircularQueue","enQueue","Rear","Rear","deQueue","enQueue","Rear",
        "deQueue","Front","deQueue","deQueue","deQueue"]
[[6],[6],[],[],[],[5],[],[],[],[],[],[]]
q = MyCircularQueue(3)
print(q.enQueue(2))
print(q.Rear())
print(q.Front())
#  print(q.Rear())
#  print(q.deQueue())
#  print(q.enQueue(5))
#  print(q.Rear())
#  print(q.deQueue())
#  print(q.Front())
#  print(q.deQueue())
#  print(q.deQueue())
#  print(q.deQueue())
