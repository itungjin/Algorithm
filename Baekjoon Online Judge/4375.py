# 구현, 수학

while True:
    try:
        n = int(input())

        number = 1
        while number % n != 0:
            number = number * 10 + 1

        print(len(str(number)))

    except:
        break
