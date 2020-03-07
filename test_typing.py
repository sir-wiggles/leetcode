from typing import Deque
from collections import deque

def foo():

    test: Deque = deque()
    test.append(10)
    test.popleft()
    print(test)

class Foo:

    def test(self) -> int:
        return 10




foo()

bar = Foo().test()
