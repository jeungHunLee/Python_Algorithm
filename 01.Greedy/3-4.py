# 문제 3-4 1이 될때 까지
# 나의 답
n, k = map(int, input().split())
count = 0

while n != 1:
    if n % k != 0:
        n -= 1
        count += 1
    elif n % k == 0:
        n //= k
        count += 1

print(count)

# 예시 답
n, k = map(int, input().split())
result = 0
while True:
    target = (n // k) * k
    result += (n - target)
    n = target

    if n < k:
        break

    n //= k
    result += 1

result += n - 1
print(result)