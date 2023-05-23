# 정렬

def solution(N, stages):
    blocked = [0] * (N + 2)
    for stage in stages:
        blocked[stage] += 1
    answer = []

    reached = len(stages)
    for i in range(1, N + 1):
        reached -= blocked[i - 1]
        if reached:
            answer.append((blocked[i] / reached, i))
        else:
            answer.append((0, i))
    answer.sort(reverse=True, key=lambda item: (item[0], -item[1]))
    answer = [item[1] for item in answer]

    return answer


solution(5, [2, 1, 2, 6, 2, 4, 3, 3])
