from typing import List
from collections import deque, defaultdict

class Solution:

    def isPossible(self, nums: List[int]) -> bool:

        m = {}
        for n in nums:
            # Get the list of sequences ending with the number n-1
            seqs = m.get(n - 1, deque())

            # If there was a list of sequences ending with n-1 then we can add
            # this number to the shortest sequense in the list of sequences.
            if len(seqs):
                seq = seqs.popleft()
                seq.append(n)

                # Get the list of sequences with the new ending number n and 
                # append the sequense to this list
                last = m.get(n, deque())
                last.append(seq)

                # If n didn't exist in the map then add it 
                m[n] = last
                continue

            # There was no last sequense found with n-1 so we can create a new
            seqs = m.get(n, deque())
            if len(seqs) == 0:
                m[n] = seqs
            seqs.appendleft([n])
        
        for seqs in m.values():
            for seq in seqs:
                if len(seq) < 3:
                    return False
        return True

t = [1,2,3,3,4,5]
print(Solution().isPossible(t), True)

t = [1,2,3,3,4]
print(Solution().isPossible(t), False)

t = [1, 1, 1, 2, 2, 2, 3, 3, 3]
print(Solution().isPossible(t), True)

t = [4,5,6,7,7,8,8,9,10,11]
print(Solution().isPossible(t), True)
