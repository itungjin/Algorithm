from collections import deque

arr = [3, 2, 7, 116, 62, 235, 1, 23, 55, 77]
n = 10
q = deque(arr)


def radix_sort():
    operand = 1
    max_val = max(arr)
    while operand < max_val:
        temp = [[] for _ in range(10)]
        while q:
            num = q.popleft()
            temp[(num // operand) % 10].append(num)
        for i in range(10):
            for num in temp[i]:
                q.append(num)
        operand *= 10


radix_sort()
print(q)
