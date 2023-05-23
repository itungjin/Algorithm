# 그리디
# N은 초깃값, K는 나누는 수
# K로 나누어질 때 N을 나누고, K로 나누어떨어질 때까지 1을 빼는 과정을 반복

n, k = map(int, input().split())
answer = 0

while (n != 1):
    if (n % k == 0):
        answer += 1
        n //= k
    else:
        if (n > k):
            answer += n % k
            n -= n % k
        else:
            answer += n - 1
            break

print(answer)
