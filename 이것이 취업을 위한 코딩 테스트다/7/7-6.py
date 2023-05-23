N = int(input())
store = [False] * 1000001
for item in list(map(int, input().split())):
    store[item] = True
M = int(input())
order = list(map(int, input().split()))

for item in order:
    if store[item]:
        print('yes', end=' ')
    else:
        print('no', end=' ')
