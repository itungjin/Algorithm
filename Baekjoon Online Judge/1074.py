N, r, c = map(int, input().split())

count = -1

visit = ((0, 0), (0, 1), (1, -1), (0, 1))


def search(n, a, b):
    global count
    if n == 1:
        for i in range(4):
            count += 1
            a, b = a + visit[i][0], b + visit[i][1]
            if a == r and b == c:
                print(count)
                return
    else:
        temp = 2 ** (n - 1)
        if a <= r < a + temp and b <= c < b + temp:
            search(n - 1, a, b)
        elif a <= r < a + temp and b + temp <= c < b + 2 * temp:
            count += temp * temp
            search(n - 1, a, b + temp)
        elif a + temp <= r < a + 2 * temp and b <= c < b + temp:
            count += temp * temp * 2
            search(n - 1, a + temp, b)
        else:
            count += temp * temp * 3
            search(n - 1, a + temp, b + temp)


search(N, 0, 0)
