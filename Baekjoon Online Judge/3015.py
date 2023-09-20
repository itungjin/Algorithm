import sys

input = sys.stdin.readline

N = int(input().rstrip())
heights = [int(input().rstrip()) for _ in range(N)]
stack = []
answer = 0
for i in range(N):
    count = 0
    count_same = 0
    if stack:
        while stack and heights[i] >= stack[-1][0]:
            if heights[i] == stack[-1][0]:
                count_same += stack[-1][1]
            else:
                count += stack[-1][1]
            stack.pop()
    if stack:
        count += 1
    if count_same > 0:
        stack += [(heights[i], count_same + 1)]
    else:
        stack += [(heights[i], 1)]
    answer += count + count_same

print(answer)
