# 구현

max = -1
row = 0
col = 0
for r in range(9):
    for c, number in enumerate(list(map(int, input().split()))):
        if number > max:
            max = number
            row, col = r+1, c+1

print(max)
print(row, col)
1
