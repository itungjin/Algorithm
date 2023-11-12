import heapq
INF = int(1e9)

TC = int(input())
for i in range(1, TC + 1):
    N, K = map(int, input().split())
    tile = [list(map(int, input().split())) for _ in range(N)]

    answer = INF
    heap = []
    tile_num_to_pos = [[] for _ in range(K + 1)]
    for r in range(N):
        for c in range(N):
            if tile[r][c] == 1:
                heapq.heappush(heap, (0, r, c))
            tile_num_to_pos[tile[r][c]].append((r, c))
    distance = [[INF] * N for _ in range(N)]
    while heap:
        dist, r, c = heapq.heappop(heap)
        if dist > distance[r][c]:
            continue
        if tile[r][c] == K:
            answer = min(answer, dist)
            continue
        for nr, nc in tile_num_to_pos[tile[r][c] + 1]:
            ndist = dist + abs(nr - r) + abs(nc - c)
            if ndist < distance[nr][nc]:
                heapq.heappush(heap, (ndist, nr, nc))
                distance[nr][nc] = ndist

    if answer == INF:
        answer = -1
    print(f'#{i} {answer}')
