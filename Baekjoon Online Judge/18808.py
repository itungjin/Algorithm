# 가로, 세로, 스태커 개수
N, M, K = map(int, input().split())
notebook = [[0] * M for _ in range(N)]
R, C = [0] * K, [0] * K
stickers = [[]] * K

for i in range(K):
    R[i], C[i] = map(int, input().split())
    stickers[i] = [list(map(int, input().split())) for _ in range(R[i])]

answer = 0


def rotation(i):
    temp = [[0] * R[i] for _ in range(C[i])]
    for r in range(R[i]):
        for c in range(C[i]):
            temp[c][R[i] - 1 - r] = stickers[i][r][c]
    stickers[i] = temp
    R[i], C[i] = C[i], R[i]


def verify(i, dr, dc):
    global answer
    temp = []
    for r in range(R[i]):
        for c in range(C[i]):
            if stickers[i][r][c] == 1:
                if notebook[dr + r][dc + c] == 1:
                    for a, b in temp:
                        notebook[a][b] = 0
                    return False
                else:
                    notebook[dr + r][dc + c] = 1
                    temp.append((dr + r, dc + c))
    answer += len(temp)
    return True


def init(i):
    for dr in range(N - R[i] + 1):
        for dc in range(M - C[i] + 1):
            if verify(i, dr, dc):
                return
    for j in range(3):
        rotation(i)
        for dr in range(N - R[i] + 1):
            for dc in range(M - C[i] + 1):
                if verify(i, dr, dc):
                    return


for i in range(K):
    init(i)

print(answer)
