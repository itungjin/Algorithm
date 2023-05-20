# 구현

# '('와 ')'의 갯수가 같다면 균형잡힌 괄호 문자열
# 균형잡힌 괄호 문자열의 괄호의 짝이 모두 맞으면 올바른 괄호 문자열
# 매개변수 p가 균형잡힌 괄호 문자열일 때 문제에 주어진 알고리즘을 통해 올바른 괄호 문자열로 변환한다.

def is_balanced(p):
    num_left, num_right = 0, 0
    for char in p:
        if char == '(':
            num_left += 1
        else:
            num_right += 1
    if num_left == num_right:
        return True
    else:
        return False


# p는 빈 문자열이 아니라고 가정한다.
def is_proper(p):
    if p[0] == ')':
        return False
    stack = list(p[0])
    index = 1
    while stack:
        if p[index] == ')':
            stack.pop()
        else:
            stack.append(p[index])
        index += 1
    if index == len(p):
        return True
    else:
        return False


def algorithm(w):
    # 입력이 빈 문자열인 경우, 빈 문자열을 반환한다.
    if not w:
        return ''
    # 만약 w가 이미 올바른 괄호 문자열이라면 그대로 return 하면 된다.
    if is_proper(w):
        return w
    # 문자열 w를 두 균형잡힌 괄호 문자열 u, v로 분리한다.
    # 단, u는 균형잡힌 괄호 문자열로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있다.
    u, v = '', ''
    for index in range(2, len(w) + 1, 2):
        u, v = w[0:index], w[index: len(w)]
        if is_balanced(u):
            break
    # 문자열 u가 올바른 괄호 문자열이라면 문자열 v에 대해 1단계부터 다시 수행한다.
    # 수행한 결과 문자열을 u에 이어 붙인 후 반환한다.
    if is_proper(u):
        return u + algorithm(v)
    # 문자열 u가 올바른 괄호 문자열이 아니라면 아래 과정을 수행한다.
    # 빈 문자열에 첫 번째 문자로 '('를 붙인다.
    # 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙인다.
    answer = f'({algorithm(v)})'
    # u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙인다.
    u = u[1:len(u) - 1]
    u = ['(' if u[index] == ')' else ')'for index in range(len(u))]
    u = "".join(u)
    answer = f'{answer}{u}'
    return answer


def solution(p):
    return (algorithm(p))
