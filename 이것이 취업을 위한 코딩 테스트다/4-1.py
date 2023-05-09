# 구현
# 시뮬레이션
# N은 정사각형 공간의 크기
# 좌표가 1에서 N까지 갖도록 정의

n = int(input())
plans = input().split()
position = [1, 1]
moves = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}

for plan in plans:
    if 1 <= position[0] + moves[plan][0] <= n and 1 <= position[1] + moves[plan][1] <= n:
        position = [position[0] + moves[plan][0], position[1] + moves[plan][1]]

print(position[0], position[1])