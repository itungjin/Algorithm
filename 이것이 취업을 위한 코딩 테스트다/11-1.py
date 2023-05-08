# 그리디
# N은 모험가의 수
# 공포도 X인 사람은 X명 이상의 그룹에 참여
# 공포도가 낮은 사람 부터 높은 사람 순으로 정렬 후 그룹 형성

n = int(input())
fear_degrees = list(map(int, input().split()))
answer = 0

fear_degrees.sort()
group_mem_num = 0
for i in range(n):
    group_mem_num += 1
    if fear_degrees[i] <= group_mem_num:
        answer += 1
        group_mem_num = 0

print(answer)
