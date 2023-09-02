chess = [[0] * 15 for _ in range(15)]
is_used_c = [False] * 15
is_used_diag_left = [False] * 29
is_used_diag_right = [False] * 29
N = int(input())
ans = 0


def recursion(r):
    if r == N:
        global ans
        ans += 1
        return

    for j in range(N):
        if not is_used_c[j] and not is_used_diag_left[N - r + j - 1] and not is_used_diag_right[r + j]:
            is_used_c[j] = True
            is_used_diag_left[N - r + j - 1] = True
            is_used_diag_right[r + j] = True
            recursion(r + 1)
            is_used_c[j] = False
            is_used_diag_left[N - r + j - 1] = False
            is_used_diag_right[r + j] = False


recursion(0)
print(ans)
