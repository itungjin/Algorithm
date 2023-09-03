A, B, C = map(int, input().split())


def solution(a, b):
    if b == 1:
        return a % C

    if b % 2 == 0:
        return solution(a * a % C, b // 2)
    else:
        return solution(a * a % C, b // 2) * a % C


print(solution(A, B))
