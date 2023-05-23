# 정렬
import sys

N = int(input())
students = [0] * N
for i in range(N):
    name, kor, eng, math = sys.stdin.readline().split()
    students[i] = [name, int(kor), int(eng), int(math)]

students.sort(key=lambda student: (
    -student[1], student[2], -student[3], student[0]))
for student in students:
    print(student[0])
