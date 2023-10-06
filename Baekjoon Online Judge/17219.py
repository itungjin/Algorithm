import sys

input = sys.stdin.readline

N, M = map(int, input().split())
keychain = dict()
for _ in range(N):
    site_address, password = input().split()
    keychain[site_address] = password
for _ in range(M):
    site_address = input().rstrip()
    print(keychain[site_address])
