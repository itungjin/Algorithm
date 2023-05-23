# 구현
# DFS

# N개의 수로 이루어진 수열이 주어진다.
# N-1개의 연산자가 주어진다. 연산자는 덧셈, 뺄셈, 곱셈, 나눗셈 4가지 종류.
# 나눗셈은 몫만을 취한다.
# 연산자 우선순위를 무시한다.

N = int(input())
A = list(map(int, input().split()))
operators = list(map(int, input().split()))
operators_permutations = set()


def dfs(n, operators_permutation):
    if n == 0:
        operators_permutations.add("".join(operators_permutation))
    else:
        for i in range(4):
            if operators[i] > 0:
                operators[i] -= 1
                operators_permutation.append(str(i))
                dfs(n - 1, operators_permutation)
                operators_permutation.pop()
                operators[i] += 1


dfs(N - 1, list())
operators_permutations = list(operators_permutations)


def evaluate(operator, operand_pre, operand_post):
    if operator == '0':
        return operand_pre + operand_post
    elif operator == '1':
        return operand_pre - operand_post
    elif operator == '2':
        return operand_pre * operand_post
    else:
        if operand_pre < 0:
            if operand_post > 0:
                return -(-operand_pre // operand_post)
        return operand_pre // operand_post


result = A[0]
for i in range(N - 1):
    result = evaluate(operators_permutations[0][i], result, A[i + 1])
max_value = result
min_value = result

for i in range(1, len(operators_permutations)):
    result = A[0]
    for j in range(N - 1):
        result = evaluate(operators_permutations[i][j], result, A[j + 1])
    max_value = max(max_value, result)
    min_value = min(min_value, result)

print(max_value)
print(min_value)
