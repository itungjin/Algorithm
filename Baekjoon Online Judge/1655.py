import heapq
import sys
input = sys.stdin.readline

N = int(input().rstrip())
hf = []
he = []
mid = [int(input().rstrip())]
print(mid[0])
for i in range(N - 1):
    num = int(input().rstrip())
    # 짝수개
    if i % 2 == 0:
        if hf and he:
            if mid[0] >= num:
                if num >= -hf[0]:
                    heapq.heappush(mid, num)
                else:
                    heapq.heappush(mid, -heapq.heappushpop(hf, -num))
            else:
                if num <= he[0]:
                    heapq.heappush(mid, num)
                else:
                    heapq.heappush(mid, heapq.heappushpop(he, num))
        else:
            heapq.heappush(mid, num)
        print(mid[0])
    # 홀수개
    else:
        heapq.heappush(mid, num)
        heapq.heappush(hf, -heapq.heappop(mid))
        heapq.heappush(he, mid.pop())
        print(mid[0])



