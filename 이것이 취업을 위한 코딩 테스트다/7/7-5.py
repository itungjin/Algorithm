def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


N = int(input())
store = list(map(int, input().split()))
M = int(input())
order = list(map(int, input().split()))

for item in order:
    index = binary_search(store, item, 0, N - 1)
    if index:
        print('yes', end=' ')
    else:
        print('no', end=' ')
