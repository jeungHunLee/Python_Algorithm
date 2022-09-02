# 볼링공 고르기
# 나의 풀이
n, m = map(int, input().split())
data = list(map(int, input().split()))
count = 0

for i in range(n - 1):
    for j in range(i + 1, n):
        if data[i] != data[j]:
            count += 1

print(count)

# 예시 풀이
n, m = map(int, input().split())
data = list(int, input().split())

# 1에서 10까지 무게에 대한 개수를 저장할 리스트
array = [0] * 10

for x in data:
    array[x] += 1   # 각 무게에 해당하는 개수 카운트

result = 0
for i in range(1, m + 1):
    n -= array[i]   # 무게가 i인 공을 선택하는 경우의 수 제거
    result += array[i] * n  # 무게가 i인 공을 선택하는 모든 경우의 수

print(result)