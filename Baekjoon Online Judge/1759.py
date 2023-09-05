vowel = ['a', 'e', 'i', 'o', 'u']
consonant = [chr(a) for a in range(ord('a'), ord('z') + 1) if chr(a) not in vowel]

L, C = map(int, input().split())
a = input().split()
a.sort()
answer = ['0'] * L


def solution(n, i):
    if n == L:
        cv = 0
        cc = 0
        for alphabet in answer:
            if alphabet in vowel:
                cv += 1
            else:
                cc += 1
        if cv >= 1 and cc >= 2:
            print("".join(answer))
        return

    for j in range(i, C):
        answer[n] = a[j]
        solution(n + 1, j + 1)


solution(0, 0)
