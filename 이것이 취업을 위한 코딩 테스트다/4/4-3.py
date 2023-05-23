# 구현
# 시뮬레이션
# 왕실 정원은 8 × 8 좌표 평면
# 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기 - 4가지
# 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기 - 4가지

position = input()
moves = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
answer = 0

position = [int(position[1]), ord(position[0]) - ord("a") + 1]
for move in moves:
    if 1 <= position[0] + move[0] <= 8 and 1 <= position[1] + move[1] <= 8:
        answer += 1

print(answer)
