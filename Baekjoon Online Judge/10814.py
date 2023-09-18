import sys

input = sys.stdin.readline

N = int(input().rstrip())
members = [0] * N
for i in range(N):
    age, name = input().split()
    age = int(age)
    members[i] = [age, name]


def merge(start, end):
    mid = (start + end) // 2
    idx_l = start
    idx_r = mid
    tmp = [0] * (end - start)
    for i in range(len(tmp)):
        if idx_l == mid:
            tmp[i] = members[idx_r]
            idx_r += 1
        elif idx_r == end:
            tmp[i] = members[idx_l]
            idx_l += 1
        elif members[idx_l][0] > members[idx_r][0]:
            tmp[i] = members[idx_r]
            idx_r += 1
        else:
            tmp[i] = members[idx_l]
            idx_l += 1

    for i in range(len(tmp)):
        members[start + i] = tmp[i]


def merge_sort(start, end):
    if start + 1 >= end:
        return
    mid = (start + end) // 2
    merge_sort(start, mid)
    merge_sort(mid, end)
    merge(start, end)


merge_sort(0, len(members))
for member in members:
    print(member[0], member[1])
