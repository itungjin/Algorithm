import sys

input = sys.stdin.readline
N = int(input().rstrip())
cards = list(map(int, input().split()))
M = int(input().rstrip())
nums = list(map(int, input().split()))
cards.sort()


def binary_search(n):
    start = 0
    end = N - 1
    while start <= end:
        mid = (start + end) // 2
        if cards[mid] == n:
            return True
        elif cards[mid] > n:
            end = mid - 1
        else:
            start = mid + 1
    return False


for num in nums:
    if binary_search(num):
        print(1, end=' ')
    else:
        print(0, end=' ')
