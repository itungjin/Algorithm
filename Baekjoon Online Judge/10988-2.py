# 구현

word = input()

reverse_word = list(word)
reverse_word.reverse()
reverse_word = "".join(reverse_word)

if word == reverse_word:
    print(1)
else:
    print(0)
