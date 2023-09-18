arr = [3, 2, 7, 116, 62, 235, 1, 23, 55, 77]
n = 10
for i in range(n - 1, -1, -1):
    max_idx = i
    for j in range(i - 1, -1, -1):
        if arr[j] > arr[max_idx]:
            max_idx = j
    arr[i], arr[max_idx] = arr[max_idx], arr[i]
print(arr)
