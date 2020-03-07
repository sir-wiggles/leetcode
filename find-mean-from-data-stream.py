import heapq

class MedianFinderV0:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.array = []


    def addNum(self, num: int) -> None:
        self.array.append(num)


    def findMedian(self) -> float:
        self.array.sort()
        size = len(self.array)

        mid = size // 2
        if size % 2 == 0:
            return (self.array[mid] + self.array[mid - 1]) / 2
        return self.array[mid]

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """

        # any value pushed to the lower will need to be negated because 
        # python doesn't have a max-heap by default 
        self.lower = [] # store the lower half of the numbers max-heap

        # python default heap is a min heap, no extra work needed to use it 
        self.upper = [] # store the upper half of the numbers min-heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lower, -num)
        heapq.heappush(self.upper, -heapq.heappop(self.lower))

        if len(self.lower) < len(self.upper):
            heapq.heappush(self.lower, -heapq.heappop(self.upper))

    def findMedian(self) -> float:
        if len(self.lower) > len(self.upper):
            return -self.lower[0]
        return (-self.lower[0] + self.upper[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
test = [41, 35, 62, 5, 97, 108]
for i in test:
    obj.addNum(i)
    print(obj.findMedian())

print(obj.lower)
print(obj.upper)
