def solution(a, b, g, s, w, t):
    n = len(g)
    start, end = 0, int(1e16)
    while start < end:
        mid = (start + end) // 2
        gold, silver, total = 0, 0, 0
        for i in range(n):
            if mid % (2 * t[i]) >= t[i]:
                move = mid // (2 * t[i]) + 1
            else:
                move = mid // (2 * t[i])
            gold += min(g[i], w[i] * move)
            silver += min(s[i], w[i] * move)
            total += min(g[i] + s[i], w[i] * move)
        if gold >= a and silver >= b and total >= a + b:
            end = mid
        else:
            start = mid + 1
    answer = end
    return answer