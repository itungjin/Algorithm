N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
answer = [0] * M


def solution(n, i):
    if n == M:
        print(*answer)
        return

    for j in range(i, N):
        answer[n] = arr[j]
        solution(n + 1, j)


solution(0, 0)
