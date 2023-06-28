# 구현

operand_first = int(input())
operand_second = int(input())

print(operand_first * (operand_second % 10))
print(operand_first * (operand_second % 100 // 10))
print(operand_first * (operand_second // 100))
print(operand_first * operand_second)
