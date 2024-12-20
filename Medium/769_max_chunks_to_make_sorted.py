"""
Task:
    You are given an integer array arr of length n
    that represents a permutation of the integers in the range [0, n - 1].
    We split arr into some number of chunks (i.e., partitions),
    and individually sort each chunk. After concatenating them, the result should equal the sorted array.
    Return the largest number of chunks we can make to sort the array.

 Topics:
    Array, Stack, Greedy, Sorting, Monotonic Stack
"""
class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        chunks = 0
        max_num = 0
        for i in range(len(arr)):
            num = arr[i]
            max_num = max(num, max_num)
            if i == max_num:
                chunks += 1

        return chunks


sol = Solution()
print(sol.maxChunksToSorted([4,3,2,1,0]))
