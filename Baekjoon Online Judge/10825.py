import sys

input = sys.stdin.readline


def sort_order(i):
    return (-i[1], i[2], -i[3], i[0])


N = int(input().rstrip())
students = [0] * N
for i in range(N):
    name, kor, eng, math = input().split()
    kor, eng, math = map(int, [kor, eng, math])
    students[i] = [name, kor, eng, math]
students.sort(key=sort_order)
for student in students:
    print(student[0])
