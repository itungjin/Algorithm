import sys

input = sys.stdin.readline

N = int(input())
max_value = 0
max_store = []
count = dict()
max_index = 0
for _ in range(N):
    num = int(input().rstrip())
    if num not in count:
        count[num] = 0
    if count[num] + 1 > max_value:
        count[num] += 1
        max_value = count[num]
        max_store.clear()
        max_store = [num]
    elif count[num] + 1 == max_value:
        count[num] += 1
        max_store.append(num)
    else:
        count[num] += 1
max_store.sort()
print(max_store[0])
