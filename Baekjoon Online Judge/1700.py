import sys

input = sys.stdin.readline

N, K = map(int, input().split())
e = list(map(int, input().split()))
m = set()
i = 0
while i < K and len(m) < N:
    m.add(e[i])
    i += 1
ans = 0

while i < K:
    # 플러그를 뽑을 필요가 없는 경우
    if e[i] in m:
        i += 1
        continue
    # 플러그를 뽑아야 하는 경우
    temp = set([x for x in m])
    for j in range(i + 1, K):
        if len(temp) == 1:
            break
        if e[j] in temp:
            temp.remove(e[j])
    m.remove(list(temp)[0])
    m.add(e[i])
    ans += 1
    i += 1
print(ans)
