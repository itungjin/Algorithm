arr = [3, 2, 7, 116, 62, 235, 1, 23, 55, 77]
n = 10


def merge(start, end):
    mid = (start + end) // 2
    tmp = [0] * (end - start)
    l_idx = start
    r_idx = mid
    for i in range(len(tmp)):
        if l_idx == mid:
            tmp[i] = arr[r_idx]
            r_idx += 1
        elif r_idx == end:
            tmp[i] = arr[l_idx]
            l_idx += 1
        elif arr[l_idx] < arr[r_idx]:
            tmp[i] = arr[l_idx]
            l_idx += 1
        else:
            tmp[i] = arr[r_idx]
            r_idx += 1
    for i in range(len(tmp)):
        arr[start + i] = tmp[i]


def merge_sort(start, end):
    if start == end - 1:
        return
    mid = (start + end) // 2
    merge_sort(start, mid)
    merge_sort(mid, end)
    merge(start, end)


merge_sort(0, n)
print(arr)
