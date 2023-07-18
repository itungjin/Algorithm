# 구현

string = input()

for char in string:
    print(ord(char) - ord('A') + 1, end=' ')
print()
