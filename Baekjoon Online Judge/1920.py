import sys

input = sys.stdin.readline

N = int(input().rstrip())
A = list(map(int, input().split()))
A.sort()
M = int(input().rstrip())
B = list(map(int, input().split()))


def binary_search(start, end, value):
    while start <= end:
        mid = (start + end) // 2
        if A[mid] == value:
            return True
        elif A[mid] < value:
            start = mid + 1
        else:
            end = mid - 1
    return False


for b in B:
    if binary_search(0, len(A) - 1, b):
        print(1)
    else:
        print(0)
