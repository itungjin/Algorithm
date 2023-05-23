N, M = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)
start = 0
end = data[0]

while start <= end:
    mid = (start + end) // 2
    total = 0

    for item in data:
        if item > mid:
            total += item - mid
        else:
            break

    available = []

    if total > M:
        available.append(mid)
        start = mid + 1
    elif total == M:
        available.append(mid)
        break
    else:
        end = mid - 1

print(min(available))
