S = input()
suffixs = [0] * len(S)
for i in range(len(S)):
    suffixs[i] = S[i:]
suffixs.sort()
for suffix in suffixs:
    print(suffix)
