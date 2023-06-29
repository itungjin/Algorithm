# 구현

chess_piece = [1, 1, 2, 2, 2, 8]

white_piece = list(map(int, input().split()))

for i in range(len(chess_piece)):
    print(chess_piece[i] - white_piece[i], end=' ')
