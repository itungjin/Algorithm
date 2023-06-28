# 구현

max_natural_number = 0
index = -1
for i in range(1, 10):
    natural_number = int(input())
    if natural_number > max_natural_number:
        max_natural_number = natural_number
        index = i

print(max_natural_number)
print(index)
