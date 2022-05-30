# 큰 수의 법칙
n, m, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)  # 내림 차순 정렬

first = a[0]
second = a[1]

result = 0

while True:
    for _ in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)
