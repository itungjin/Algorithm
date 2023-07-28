# 연결 리스트

import sys
input = sys.stdin.readline

MAX_LENGTH = 1000001

test_case = int(input().rstrip())
for _ in range(test_case):
    string = input().rstrip()

    data = [0] * MAX_LENGTH
    prev = [-1] * MAX_LENGTH
    next = [-1] * MAX_LENGTH
    unused = 1
    curr = 0

    def insert(pos, item):
        global unused
        data[unused] = item
        prev[unused] = pos
        next[unused] = next[pos]
        next[pos] = unused
        if next[unused] != -1:
            prev[next[unused]] = unused
        unused += 1

    def erase(pos):
        next[prev[pos]] = next[pos]
        if next[pos] != -1:
            prev[next[pos]] = prev[pos]

    for char in string:
        if char == '<':
            if prev[curr] != -1:
                curr = prev[curr]
        elif char == '>':
            if next[curr] != -1:
                curr = next[curr]
        elif char == '-':
            if prev[curr] != -1:
                erase(curr)
                curr = prev[curr]
        else:
            insert(curr, char)
            curr = next[curr]

    curr = next[0]
    while curr != -1:
        print(data[curr], end='')
        curr = next[curr]
    print()
