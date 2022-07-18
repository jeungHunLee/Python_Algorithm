# 05-07 (연산자 끼워 넣기)
import itertools
import copy

n = int(input())
numbers = list(map(int, input().split()))

operator_num = list(map(int, input().split()))
operators = []
for i in range(4):
    if i == 0:
        for _ in range(operator_num[i]):
            operators.append('+')
    elif i == 1:
        for _ in range(operator_num[i]):
            operators.append('-')
    elif i == 2:
        for _ in range(operator_num[i]):
            operators.append('*')
    else:
        for _ in range(operator_num[i]):
            operators.append('/')

operator_permutation = list(itertools.permutations(operators, n - 1))
answer = []
for case in operator_permutation:
    numbers_operator = copy.deepcopy(numbers)
    j = 1
    for i in range(n-1):
        numbers_operator.insert(j, case[i])
        j += 2

    result = numbers_operator[0]
    for i in range(1, len(numbers_operator), 2):
        if numbers_operator[i] == '+':
            result += numbers_operator[i+1]
        elif numbers_operator[i] == '-':
            result -= numbers_operator[i+1]
        elif numbers_operator[i] == '*':
            result *= numbers_operator[i+1]
        elif numbers_operator[i] == '/':
            if result < 0:
                result = -(-result // numbers_operator[i+1])
            else:
                result //= numbers_operator[i+1]

    answer.append(result)

print(max(answer))
print(min(answer))
