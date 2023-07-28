# 구현
# 연결 리스트

import sys
input = sys.stdin.readline

string = input().rstrip()
N = len(string)

data = [0] * 600001
prev = [-1] * 600001
next = [-1] * 600001
unused = N+1
cursor = N

for i in range(N):
    data[i+1] = string[i]
    next[i] = i+1
    prev[i+1] = i


def delete(cursor):
    next[prev[cursor]] = next[cursor]
    if next[cursor] != -1:
        prev[next[cursor]] = prev[cursor]
    return prev[cursor]


def insert(cursor, value):
    global unused

    data[unused] = value
    prev[unused] = cursor
    next[unused] = next[cursor]

    next[cursor] = unused
    if next[unused] != -1:
        prev[next[unused]] = unused

    unused += 1

    return unused - 1


M = int(input().rstrip())
for _ in range(M):
    command = input().rstrip()

    if command[0] == 'L':
        if cursor != 0:
            cursor = prev[cursor]
    elif command[0] == 'D':
        if next[cursor] != -1:
            cursor = next[cursor]
    elif command[0] == 'B':
        if cursor != 0:
            cursor = delete(cursor)
    else:
        cursor = insert(cursor, command[2])


curr = next[0]
while curr != -1:
    print(data[curr], end='')
    curr = next[curr]
