
class Node(object):
    def __init__(self, value, prev=None):
        self.value = value
        self.prev = prev
        self.next = None

    def __repr__(self):
        return str(self.value)

class List(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, value):
        node = Node(value, self.head)
        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def reverse(self):
        prev = None
        current = self.head
        next = None

        while current is not None:
            next = current.next
            current.next = prev
            current.prev = next
            prev = current

            current = next
        self.head = prev




if __name__ == "__main__":
    l = List()
    print(list(l))
    l.push(10)
    l.push(20)
    l.push(30)
    l.push(40)

    print(list(l))

    l.reverse()
    print(list(l))
