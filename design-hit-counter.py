from collections import deque

class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = deque()


    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.queue.append(timestamp)


    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        while self.queue:
            if timestamp - self.queue[0] >= 300:
                self.queue.popleft()
            else:
                break
        return len(self.queue)



# Your HitCounter object will be instantiated and called as such:
counter = HitCounter()
# hit at timestamp 1.
counter.hit(1)

# hit at timestamp 2.
counter.hit(2)

# hit at timestamp 3.
counter.hit(3)

# get hits at timestamp 4, should return 3.
counter.getHits(4) == 4

# hit at timestamp 300.
counter.hit(300)

# get hits at timestamp 300, should return 4.
counter.getHits(300) == 4

# get hits at timestamp 301, should return 3.
print(counter.getHits(301))
