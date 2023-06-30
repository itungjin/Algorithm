# 구현

word = input()

croatia_alphabets = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

answer = len(word)
for croatia_alphabet in croatia_alphabets:
    if len(croatia_alphabet) == 2:
        answer -= word.count(croatia_alphabet)
    else:
        answer -= 2 * word.count(croatia_alphabet)
# "dz=" 알파벳이 있을 때 "z=" 알파벳이 있다고 중복으로 인식하게 된다.
# 따라서 "z=" 알파벳이 더 있다고 판단하여 word.count("dz=")를 더 빼준 것을 다시 더한다.
if word.count("dz=") > 0:
    answer += word.count("dz=")

print(answer)
