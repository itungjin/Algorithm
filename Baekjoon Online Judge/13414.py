import sys

input = sys.stdin.readline

K, L = map(int, input().split())
student_numbers = dict()
waiting_list = [0] * L
for i in range(L):
    student_number = input().rstrip()
    waiting_list[i] = student_number
    if student_number in student_numbers:
        student_numbers[student_number] += 1
    else:
        student_numbers[student_number] = 1
count = 0
for i in range(L):
    if student_numbers[waiting_list[i]] != 1:
        student_numbers[waiting_list[i]] -= 1
    else:
        print(waiting_list[i])
        count += 1
    if count == K:
        break
