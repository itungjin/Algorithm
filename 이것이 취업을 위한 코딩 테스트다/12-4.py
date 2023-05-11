# 구현
# 자물쇠는 N × N 크기, 열쇠는 M × M 크기
# 자물쇠의 영역에서 열쇠의 돌기와 자물쇠의 홈이 일치해야함
# 열쇠의 돌기와 자물쇠의 돌기가 만나면 안 됨
# key는 열쇠, lock은 자물쇠
# M <= N
# 0은 홈, 1은 돌기

def solution(key, lock):
    n = len(lock)
    num_groove = 0
    for i in range(n):
        for j in range(n):
            if lock[i][j] == 0:
                num_groove += 1

    m = len(key)
    for i in range(4):
        if i != 0:  # 시계 방향으로 90도 회전
            temp_key = [[0] * m for _ in range(m)]
            for c in range(m):
                for r in range(m):
                    temp_key[r][c] = key[m - 1 - c][r]
            key = temp_key

        for move_r in range(-m + 1, n):
            for move_c in range(-m + 1, n):
                if open_lock(key, lock, n, m, num_groove, move_r, move_c):
                    return True

    return False


def open_lock(key, lock, n, m, num_groove, move_r, move_c):
    count = 0
    for r in range(m):
        for c in range(m):
            if 0 <= r + move_r < n and 0 <= c + move_c < n:
                if key[r][c] == 1:
                    if lock[r + move_r][c + move_c] == 0:
                        count += 1
                    else:
                        return False

    if count == num_groove:
        return True
    else:
        return False
