import sys

input = sys.stdin.readline

N = int(input().rstrip())
integers = list(map(int, input().split()))
M = int(input().rstrip())
datas = list(map(int, input().split()))
integers.sort()


def binary_search_start(n):
    start = 0
    end = N
    while start < end:
        mid = (start + end) // 2
        if integers[mid] < n:
            start = mid + 1
        else:
            end = mid
    return start


def binary_search_end(n):
    start = 0
    end = N
    while start < end:
        mid = (start + end) // 2
        if integers[mid] <= n:
            start = mid + 1
        else:
            end = mid
    return start


for data in datas:
    start = binary_search_start(data)
    end = binary_search_end(data)
    print(end - start, end=' ')
