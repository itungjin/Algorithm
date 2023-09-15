import sys

input = sys.stdin.readline

n, w, L = map(int, input().split())
a = list(map(int, input().split()))

front = 0
end = -1
weight = 0
times = [0] * n
time = 0
while True:
    time += 1
    if time - times[front] == w:
        weight -= a[front]
        front += 1
        if front == n:
            break
    if end + 1 < n:
        if weight + a[end + 1] <= L and end - front + 1 < w:
            end += 1
            weight += a[end]
            times[end] = time
    if front == n:
        break

print(time)
