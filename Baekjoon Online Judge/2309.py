# 구현
# 정렬

heights = [0] * 9
for i in range(9):
    heights[i] = int(input())

heights_set = set(heights)
illegal_height = sum(heights) - 100
for height in heights:
    if illegal_height - height in heights_set and illegal_height - height != height:
        heights.remove(height)
        heights.remove(illegal_height - height)
        break

heights.sort()

for i in range(7):
    print(heights[i])
