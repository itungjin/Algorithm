# 구현
# NXN 크기의 보드
# 이동은 상하좌우 4가지 경우
# 이동시 같은 값을 갖는 블록이 만난다면 두 블록은 합쳐지나, 연쇄작용은 일어나지 않음

from collections import deque
from copy import deepcopy

n = int(input())  # 1 <= n <= 20
board = [list(map(int, input().split())) for _ in range(n)]
answer = 0


def run_2048(direction, _board, count):
    global answer
    if direction == 0:  # 위로
        for c in range(n):
            top_blank = deque()
            for r in range(n):
                if _board[r][c] == 0:
                    top_blank.append(r)
                elif len(top_blank) != 0:
                    _board[top_blank.popleft()][c] = _board[r][c]
                    _board[r][c] = 0
                    top_blank.append(r)
        for c in range(n):
            for r in range(n - 1):
                if _board[r][c] == 0:
                    break
                if _board[r][c] == _board[r + 1][c]:
                    _board[r][c] *= 2
                    for _r in range(r + 1, n - 1):
                        _board[_r][c] = _board[_r + 1][c]
                    _board[n - 1][c] = 0
    elif direction == 1:  # 오른쪽으로
        for r in range(n):
            rightmost_blank = deque()
            for c in range(n - 1, -1, -1):
                if _board[r][c] == 0:
                    rightmost_blank.append(c)
                elif len(rightmost_blank) != 0:
                    _board[r][rightmost_blank.popleft()] = _board[r][c]
                    _board[r][c] = 0
                    rightmost_blank.append(c)
        for r in range(n):
            for c in range(n - 1, 0, -1):
                if _board[r][c] == 0:
                    break
                if _board[r][c] == _board[r][c - 1]:
                    _board[r][c] *= 2
                    for _c in range(c - 1, 0, -1):
                        _board[r][_c] = _board[r][_c - 1]
                    _board[r][0] = 0
    elif direction == 2:  # 아래로
        for c in range(n):
            bottom_blank = deque()
            for r in range(n - 1, -1, -1):
                if _board[r][c] == 0:
                    bottom_blank.append(r)
                elif len(bottom_blank) != 0:
                    _board[bottom_blank.popleft()][c] = _board[r][c]
                    _board[r][c] = 0
                    bottom_blank.append(r)
        for c in range(n):
            for r in range(n - 1, 0, -1):
                if _board[r][c] == 0:
                    break
                if _board[r][c] == _board[r - 1][c]:
                    _board[r][c] *= 2
                    for _r in range(r - 1, 0, -1):
                        _board[_r][c] = _board[_r - 1][c]
                    _board[0][c] = 0
    elif direction == 3:  # 왼쪽으로
        for r in range(n):
            leftmost_blank = deque()
            for c in range(n):
                if _board[r][c] == 0:
                    leftmost_blank.append(c)
                elif len(leftmost_blank) != 0:
                    _board[r][leftmost_blank.popleft()] = _board[r][c]
                    _board[r][c] = 0
                    leftmost_blank.append(c)
        for r in range(n):
            for c in range(n - 1):
                if _board[r][c] == 0:
                    break
                if _board[r][c] == _board[r][c + 1]:
                    _board[r][c] *= 2
                    for _c in range(c + 1, n - 1):
                        _board[r][_c] = _board[r][_c + 1]
                    _board[r][n - 1] = 0

    count -= 1
    if count > 0:
        for i in range(4):
            __board = deepcopy(_board)
            run_2048(i, __board, count)
    else:
        for r in range(n):
            answer = max(answer, max(_board[r]))


for i in range(4):
    _board = deepcopy(board)
    run_2048(i, _board, 5)

print(answer)
