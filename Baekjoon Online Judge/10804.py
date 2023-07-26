# 구현

cards = [i for i in range(21)]

for _ in range(10):
    a, b = map(int, input().split())

    if a == b:
        pass
    else:
        cards_reverse = cards[a:b+1]
        cards_reverse.reverse()
        cards = cards[0:a] + cards_reverse + cards[b+1:21]

for i in range(1, 21):
    print(cards[i], end=' ')
