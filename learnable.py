from collections import Counter
from heapq import heapify, heappop


def nth_most_rate(list, n):
    # count number of occurences of elements in l
    count = Counter(list)
    # Load (freq, num) into nums
    nums = [(v, k) for k, v in count.items()]
    # Convert the array into a heap
    # heap priority is based on the freq of the element
    heapify(nums)

    # Track the results
    res = -1
    # Pop from our heap starting from the smallest count
    while n:
        _, res = heappop(nums)
        n -= 1
    return res


print(nth_most_rate([5, 4, 5, 4, 5, 4, 4, 5, 3, 3, 3, 2, 2, 1, 5], 2))
