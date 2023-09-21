import sys

input = sys.stdin.readline

n = int(input().rstrip())
tri = [list(map(int, input().split())) for _ in range(n)]
odd = [tri[0][0]]
even = []
for i in range(2, n + 1):
    if i % 2 == 0:
        even = [0] * i
        even[0] = odd[0] + tri[i - 1][0]
        for j in range(1, i - 1):
            even[j] = max(odd[j - 1] + tri[i - 1][j], odd[j] + tri[i - 1][j])
        even[i - 1] = odd[i - 2] + tri[i - 1][i - 1]
    else:
        odd = [0] * i
        odd[0] = even[0] + tri[i - 1][0]
        for j in range(1, i - 1):
            odd[j] = max(even[j - 1] + tri[i - 1][j], even[j] + tri[i - 1][j])
        odd[i - 1] = even[i - 2] + tri[i - 1][i - 1]

if n % 2 == 0:
    answer = even
else:
    answer = odd
print(max(answer))
