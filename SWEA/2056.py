# 구현

def isValidDate(date):
    answer = ""
    for i in range(4):
        answer += date[i]
    answer += '/'

    month = ""
    for i in range(4, 6):
        month += date[i]
    if 1 <= int(month) <= 12:
        answer += month
    else:
        return -1
    month = int(month)
    answer += '/'

    day = ""
    for i in range(6, 8):
        day += date[i]
    if month <= 7 and month % 2 == 1 or month >= 8 and month % 2 == 0:
        if 1 <= int(day) <= 31:
            answer += day
        else:
            return -1
    elif month == 4 or month == 6 or month == 9 or month == 1:
        if 1 <= int(day) <= 30:
            answer += day
        else:
            return -1
    else:
        if i <= int(day) <= 28:
            answer += day
        else:
            return -1

    return answer


T = int(input())

for test_case in range(1, T + 1):
    print('#' + str(test_case), end=' ')

    date = input()
    print(isValidDate(date))
