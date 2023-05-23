N = int(input())
store = set(list(map(int, input().split())))
M = int(input())
order = list(map(int, input().split()))

for item in order:
    if item in store:
        print('yes', end=' ')
    else:
        print('no', end=' ')
