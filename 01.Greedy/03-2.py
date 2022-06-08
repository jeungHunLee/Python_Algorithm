# 큰 수의 법칙
# 내가 푼 풀이
n, m, k = map(int, input().split())
num = list(map(int, input().split()))
num.sort()  # 오름차순 정렬
count = 0  # 가장 큰 수를 더한 횟수를 저장할 변수
result = 0

for _ in range(m):
    if count != k:
        result += num[n - 1]
        count += 1  # 가장 큰 수를 더할때 마다 횟수 +1
    else:  # 가장 큰 수를 k만큼 더하였다면
        result += num[n - 2]  # 두번째 큰 수 한번 더하기
        count = 0  # count 초기화

print(result)

# 예시 풀이
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()  # 오름차순 정렬
first = data[n - 1]  # 가장 큰 수
second = data[n - 2]  # 두 번째로 큰 수

result = 0

while True:
    for i in range(k):  # 가장 큰 수를 k번 만큼 더하기
        if m == 0:
            break
        result += first
        m -= 1  # 더할때 마다 1씩 빼기
    if m == 0:
        break
    result += second  # 두번째로 큰 수 한 번 더하기
    m -= 1

print(result)
