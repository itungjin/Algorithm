import sys

input = sys.stdin.readline

N = int(input().rstrip())
S = [list(map(int, input().split())) for _ in range(N)]
team = [0] * (N // 2)
answer = 99


def calculate():
    global answer
    t = set(team)
    s1 = 0
    s2 = 0
    for r in range(N):
        for c in range(r):
            if r in t and c in t:
                s1 += S[r][c]
                s1 += S[c][r]
            elif r not in t and c not in t:
                s2 += S[r][c]
                s2 += S[c][r]
    answer = min(answer, abs(s2 - s1))


def solution(n, m):
    if n == N // 2:
        calculate()
        return

    for i in range(m, N):
        team[n] = i
        solution(n + 1, i + 1)


solution(0, 0)
print(answer)
