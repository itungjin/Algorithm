# 구현
# 시뮬레이션
# 게임 맵 크기는 N × M

n, m = map(int, input().split())
a, b, d = map(int, input().split())
game_map = [0] * n
for i in range(n):
    game_map[i] = list(map(int, input().split()))
answer = 0

moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
turn = 0

while True:
    turn += 1
    d = (d - 1) % 4

    if turn == 4:
        next_a, next_b = a - moves[d][0], b - moves[d][1]
        if game_map[next_a][next_b] == 1:
            break
        else:
            a, b = next_a, next_b
            turn = 0
    else:
        next_a, next_b = a + moves[d][0], b + moves[d][1]
        if game_map[next_a][next_b] == 0:
            a, b = next_a, next_b
            game_map[a][b] = 2
            answer += 1
            turn = 0

print(answer)
