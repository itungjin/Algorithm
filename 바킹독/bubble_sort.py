arr = [3, 2, 7, 116, 62, 235, 1, 23, 55, 77]
n = 10
for i in range(n - 1, -1, -1):
    for j in range(i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
print(arr)
