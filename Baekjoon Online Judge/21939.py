import heapq
import sys

input = sys.stdin.readline

N = int(input().rstrip())
q = []
qr = []
count = dict()
count_reverse = dict()
ptol = dict()
to_delete = dict()
for i in range(N):
    P, L = map(int, input().split())
    heapq.heappush(q, L)
    heapq.heappush(qr, -L)
    if L in count:
        heapq.heappush(count[L], P)
        heapq.heappush(count_reverse[L], -P)
    else:
        count[L] = [P]
        count_reverse[L] = [-P]
    ptol[P] = L
M = int(input().rstrip())
for _ in range(M):
    command = input().split()
    if command[0] == "recommend":
        x = int(command[1])
        if x == 1:
            while True:
                l = -qr[0]
                if not count_reverse[l]:
                    heapq.heappop(qr)
                    continue
                while count_reverse[l] and l in to_delete and -count_reverse[l][0] in to_delete[l]:
                    heapq.heappop(count_reverse[l])
                if not count_reverse[l]:
                    heapq.heappop(qr)
                    continue
                print(-count_reverse[l][0])
                break
        else:
            while True:
                l = q[0]
                if not count[l]:
                    heapq.heappop(q)
                    continue
                while count[l] and l in to_delete and count[l][0] in to_delete[l]:
                    heapq.heappop(count[l])
                if not count[l]:
                    heapq.heappop(q)
                    continue
                print(count[l][0])
                break
    elif command[0] == "add":
        P, L = int(command[1]), int(command[2])
        heapq.heappush(q, L)
        heapq.heappush(qr, -L)
        if L in count:
            heapq.heappush(count[L], P)
            heapq.heappush(count_reverse[L], -P)
        else:
            count[L] = [P]
            count_reverse[L] = [-P]
        if L in to_delete and P in to_delete[L]:
            to_delete[L].remove(P)
        ptol[P] = L
    else:
        P = int(command[1])
        if ptol[P] in to_delete:
            to_delete[ptol[P]].add(P)
        else:
            to_delete[ptol[P]] = {P}
        del ptol[P]
