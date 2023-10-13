import sys

input = sys.stdin.readline

N = int(input().rstrip())

left = dict()
right = dict()

for _ in range(N):
    p, l, r = input().split()
    left[p] = l
    right[p] = r


def preorder(n):
    print(n, end='')
    if left[n] != '.':
        preorder(left[n])
    if right[n] != '.':
        preorder(right[n])


def inorder(n):
    if left[n] != '.':
        inorder(left[n])
    print(n, end='')
    if right[n] != '.':
        inorder(right[n])


def postorder(n):
    if left[n] != '.':
        postorder(left[n])
    if right[n] != '.':
        postorder(right[n])
    print(n, end='')


preorder('A')
print()
inorder('A')
print()
postorder('A')
print()
