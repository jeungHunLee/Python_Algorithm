# 볼링공 고르기
# 나의 풀이
n, m = map(int, input().split())
data = list(map(int, input().split()))
result = []

for i in range(len(data) - 1):
    for j in range(i+1, len(data)):
        if data[i] == data[j]:  # 같은 무게일 경우 제외
            continue
        result.append([data[i], data[j]])   # 서로 다른 무게 일때, 경우의 수 추가

print(len(result))

# 예시 풀이
n, m = map(int, input().split())
data = list(int, input().split())

# 1에서 10까지 무게에 대한 개수를 저장할 리스트
array = [0] * 10

for x in data:
    array[x] += 1   # 각 무게에 해당하는 개수 카운트

result = 0
for i in range(1, m+1):
    n -= array[i]   # 무게가 i인 공을 선택하는 경우의 수 제거
    result += array[i] * n  # 무게가 i인 공을 선택하는 모든 경우의 수

print(result)