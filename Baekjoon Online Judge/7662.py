import sys
import heapq

input = sys.stdin.readline

T = int(input().rstrip())
for _ in range(T):
    k = int(input().rstrip())
    heap = []
    heap_reverse = []
    heap_delete = dict()
    heap_reverse_delete = dict()
    length = 0
    for _ in range(k):
        opr, n = input().split()
        n = int(n)
        if opr == "I":
            heapq.heappush(heap, n)
            heapq.heappush(heap_reverse, -n)
            length += 1
        else:
            if length <= 1:
                heap.clear()
                heap_reverse.clear()
                heap_delete.clear()
                heap_reverse_delete.clear()
                length = 0
            elif n == 1:
                while heap_reverse and -heap_reverse[0] in heap_reverse_delete:
                    item = -heapq.heappop(heap_reverse)
                    if heap_reverse_delete[item] == 1:
                        del heap_reverse_delete[item]
                    else:
                        heap_reverse_delete[item] -= 1
                item = -heapq.heappop(heap_reverse)
                length -= 1
                if item in heap_delete:
                    heap_delete[item] += 1
                else:
                    heap_delete[item] = 1
            else:
                while heap and heap[0] in heap_delete:
                    item = heapq.heappop(heap)
                    if heap_delete[item] == 1:
                        del heap_delete[item]
                    else:
                        heap_delete[item] -= 1
                item = heapq.heappop(heap)
                length -= 1
                if item in heap_reverse_delete:
                    heap_reverse_delete[item] += 1
                else:
                    heap_reverse_delete[item] = 1
    if length != 0:
        while heap[0] in heap_delete:
            item = heapq.heappop(heap)
            if heap_delete[item] == 1:
                del heap_delete[item]
            else:
                heap_delete[item] -= 1
        while -heap_reverse[0] in heap_reverse_delete:
            item = -heapq.heappop(heap_reverse)
            if heap_reverse_delete[item] == 1:
                del heap_reverse_delete[item]
            else:
                heap_reverse_delete[item] -= 1
        print(-heap_reverse[0], heap[0])
    else:
        print('EMPTY')
