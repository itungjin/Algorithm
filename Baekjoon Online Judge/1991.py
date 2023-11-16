import sys

WEIGHT = ord('A')

input = sys.stdin.readline


N = int(input().rstrip())

left = [-1] * 26
right = [-1] * 26

for _ in range(N):
    p, l, r = input().split()
    if l != '.':
        left[ord(p) - WEIGHT] = ord(l) - WEIGHT
    if r != '.':
        right[ord(p) - WEIGHT] = ord(r) - WEIGHT


def pre_order(node):
    if node == -1:
        return
    print(chr(node + WEIGHT), end='')
    pre_order(left[node])
    pre_order(right[node])


def in_order(node):
    if node == -1:
        return
    in_order(left[node])
    print(chr(node + WEIGHT), end='')
    in_order(right[node])


def post_order(node):
    if node == -1:
        return
    post_order(left[node])
    post_order(right[node])
    print(chr(node + WEIGHT), end='')


pre_order(0)
print()
in_order(0)
print()
post_order(0)
