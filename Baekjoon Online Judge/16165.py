import sys

input = sys.stdin.readline

N, M = map(int, input().split())
group_to_member = dict()
member_to_group = dict()
for _ in range(N):
    group = input().rstrip()
    group_to_member[group] = []
    for _ in range(int(input().rstrip())):
        member = input().rstrip()
        group_to_member[group].append(member)
        member_to_group[member] = group
    group_to_member[group].sort()
for _ in range(M):
    question = input().rstrip()
    type = int(input().rstrip())
    if type == 0:
        for member in group_to_member[question]:
            print(member)
    else:
        print(member_to_group[question])
