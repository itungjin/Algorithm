import sys

input = sys.stdin.readline

N = int(input().rstrip())
flowers = [0] * N
for i in range(N):
    sm, sd, em, ed = list(map(int, input().split()))
    s = sm * 100 + sd
    e = em * 100 + ed
    flowers[i] = [s, e]
flowers.sort()
now = 301
next_flowers = []
answer = 0
for i in range(N):
    s, e = flowers[i]
    if now >= 1201:
        break
    # 현재 상황에서 심을 수 있는 꽃들을 모두 추가했을 때
    if s > now:
        # 심을 수 있는 꽃들이 있는 경우
        if next_flowers:
            now = max(next_flowers)
            next_flowers.clear()
            if s > now:
                answer = 0
                break
            next_flowers.append(e)
            answer += 1
        # 심을 수 있는 꽃이 없는 경우
        else:
            answer = 0
            break
    # 현재 상황에서 심을 수 있는 꽃들을 리스트에 추가한다.
    else:
        next_flowers.append(e)
if now < 1201 and next_flowers:
    now = max(next_flowers)
    answer += 1
    if now < 1201:
        answer = 0
print(answer)
