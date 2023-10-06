import sys
input = sys.stdin.readline

N = int(input().rstrip())
seq = list(map(int, input().split()))

subseq = set()
answer = 0
left = 0
right = 0
pre = 0
while True:
    if seq[right] in subseq:
        subseq.remove(seq[left])
        left += 1
        pre -= 1
        answer += pre
    else:
        answer += 1
        subseq.add(seq[right])
        right += 1
        pre += 1
        if right == N:
            answer += pre * (pre - 1) // 2
            break
print(answer)