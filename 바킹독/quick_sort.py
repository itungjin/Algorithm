arr = [3, 2, 7, 116, 62, 235, 1, 23, 55, 77]
n = 10


def quick_sort(start, end):
    if start >= end:
        return
    pivot = arr[start]
    left = start + 1
    right = end
    while True:
        while left <= end and arr[left] <= pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
        else:
            arr[start], arr[right] = arr[right], arr[start]
            break
    quick_sort(start, right - 1)
    quick_sort(right + 1, end)


quick_sort(0, n - 1)
print(arr)
