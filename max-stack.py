class MaxStack(list):
    def push(self, x):
        m = max(x, self[-1][1] if self else float('-inf'))
        self.append((x, m))

    def pop(self):
        return list.pop(self)[0]

    def top(self):
        return self[-1][0]

    def peekMax(self):
        return self[-1][1]

    def popMax(self):
        m = self[-1][1]
        b = []
        while self[-1][0] != m:
            b.append(self.pop())

        self.pop()
        for item in reversed(b):
            self.push(item)
        return m 


# Your MaxStack object will be instantiated and called as such:
operations = ["MaxStack","push","push","popMax","peekMax"]
values = [[],[5],[1],[],[]]


operations = ["MaxStack","push","push","push","top","popMax","top","peekMax","pop","top"]
values = [[],[5],[1],[5],[],[],[],[],[],[]]


#  operations = ["MaxStack","push","push","push","peekMax","popMax","popMax","top"]
#  values =     [        [],   [5],   [1],   [6],       [],      [],      [],   []]
         #   [      null,  null,  null,  null,        6,       6,       5,    1]

stack = MaxStack()
for (operation, value) in list(zip(operations, values))[1:]:
    if operation == 'push':
        print(stack.push(value[0]))
    else:
        print(stack.__getattribute__(operation)())

