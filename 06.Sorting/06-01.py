# 06-01(위에서 아래로)
n = int(input())
numbers = []

for _ in range(n):
    numbers.append(int(input()))

numbers.sort(reverse=True)

for num in numbers:
    print(num, end=" ")