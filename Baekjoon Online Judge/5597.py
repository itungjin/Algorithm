# 구현

students = {i for i in range(1, 31)}
for _ in range(28):
    students.remove(int(input()))
students = sorted(list(students))

print(students[0])
print(students[1])
