import math


def solution(n):
    temp = int(math.sqrt(n))
    if temp * temp == n:
        return (temp + 1) ** 2
    return -1

