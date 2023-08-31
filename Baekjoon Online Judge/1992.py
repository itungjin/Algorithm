N = int(input())
video = [list(map(int, input())) for _ in range(N)]
tree = ""


def check(n, a, b):
    for r in range(a, a + n):
        for c in range(b, b + n):
            if video[a][b] != video[r][c]:
                return False
    return True


def compression(n, a, b):
    global tree
    if check(n, a, b):
        tree += str(video[a][b])
    else:
        tree += '('
        n //= 2
        da = [0, 0, n, n]
        db = [0, n, 0, n]
        for i in range(4):
            compression(n, a + da[i], b + db[i])
        tree += ')'


compression(N, 0, 0)
print(tree)
