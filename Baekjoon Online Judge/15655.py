N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
answer = [0] * M


def solution(n, a):
    if n == M:
        print(*answer)
        return

    for i in range(a + 1, N + 1):
        answer[n] = arr[i - 1]
        solution(n + 1, i)


solution(0, 0)
