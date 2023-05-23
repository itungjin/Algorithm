import sys
N = int(sys.stdin.readline().rstrip())
houses = list(map(int, sys.stdin.readline().split()))
houses.sort()


def antenna(houses):
    min_dist = 0
    for house in houses:
        min_dist += abs(houses[0] - house)

    same_pos = []
    for i in range(1, N):
        dist_between = houses[i] - houses[i - 1]
        if dist_between == 0:
            same_pos.append(i - 1)
            continue
        temp_dist = min_dist + i * dist_between - (N - i) * dist_between
        if (min_dist <= temp_dist):
            if same_pos:
                print(houses[same_pos[0]])
                return
            print(houses[i - 1])
            return
        min_dist = min(min_dist, temp_dist)
        same_pos = []
    print(houses[-1])


antenna(houses)
