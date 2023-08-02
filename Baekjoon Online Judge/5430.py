import sys
from collections import deque

T = int(input())
for _ in range(T):
    p = input()
    n = int(input())
    x = sys.stdin.readline().rstrip()
    if len(x) == 2:
        x = deque()
        head = 0
        tail = 0
    else:
        x = list(map(int, (x[1:-1]).split(',')))
        head = 0
        tail = len(x)

    def ac(head, tail):
        for func in p:
            if func == 'R':
                if head < tail:
                    head, tail = tail - 1, head - 1
                elif head > tail:
                    head, tail = tail + 1, head + 1
                else:
                    pass
            else:  # func == 'D'
                if head == tail:
                    return None
                elif head < tail:
                    head += 1
                else:
                    head -= 1

        return head, tail

    result = ac(head, tail)

    if result == None:
        print('error')
    else:
        head, tail = result[0], result[1]
        if head < tail:
            x = ",".join(map(str, x[result[0]:result[1]]))
        elif head > tail:
            if tail == -1:
                x = ",".join(map(str, x[result[0]::-1]))
            else:
                x = ",".join(map(str, x[result[0]:result[1]:-1]))
        else:
            x = ''
        print(f'[{x}]')
