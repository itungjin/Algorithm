import sys

input = sys.stdin.readline
S, E, Q = input().split()
S = int("".join(S.split(':')))
E = int("".join(E.split(':')))
Q = int("".join(Q.split(':')))
name = set()
pre = set()
after = set()
while True:
    try:
        time, nickname = input().split()
        time = int("".join(time.split(':')))
        name.add(nickname)
        if time <= S:
            pre.add(nickname)
        if E <= time <= Q:
            after.add(nickname)
    except:
        break
answer = 0
for n in name:
    if n in pre and n in after:
        answer += 1
print(answer)
