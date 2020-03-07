from typing import List
from queue import PriorityQueue

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda x: x[0])
        pq = PriorityQueue()
        needed = 0
        print(intervals)
        for start, end in intervals:
            while pq.qsize() and start >= pq.queue[0]:
                pq.get()
            pq.put(end)
            needed = max(pq.qsize(), needed)
        return needed


cases = [
    [[0, 30],[5, 10],[15, 20]],
    [
        [0, 3], [1,2], [2,3], 
        [3,9],[4,5],
        [10,11]
    ],
    [[9,10],[4,9],[4,17]]
]

for case in cases:
    print(Solution().minMeetingRooms(case))
