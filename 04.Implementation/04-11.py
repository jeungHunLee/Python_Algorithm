# 04-11 (치킨 배달)
from itertools import combinations

n, m = map(int, input().split())
count = 0  # 행
chicken, house = [], []  # 치킨집 좌표, 집 좌표

for _ in range(n):
    line = list(map(int, input().split()))
    for i in range(len(line)):
        if line[i] == 2:
            chicken.append([count, i])  # 치킨 집
        elif line[i] == 1:
            house.append([count, i])  # 집
    count += 1

combination = list(combinations(chicken, m))  # 치킨 집 중 m개의 조합
result = []  # 도시의 치킨 거리

for choice in combination:
    chicken_distance = []  # 치킨 거리
    for house_point in house:
        distance = []  # 집부터 치킨 집까지의 거리
        for chicken_point in choice:
            distance.append(abs(house_point[0] - chicken_point[0]) + abs(house_point[1] - chicken_point[1]))
        chicken_distance.append(min(distance))
    result.append(sum(chicken_distance))

print(min(result))

# 예시 답안
from itertools import combinations

n, m = map(int, input().split())
chicken, house = [], []

for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append(data[c])
        elif data[c] == 2:
            chicken.append(data[c])

# 모든 치킨집 중에서 m개의 조합 개산
candidates = list(combinations(chicken, m))


# 치킨 거리의 합을 계산하는 함수
def get_sum(candidate):
    result = 0
    # 모든 집에 대하여
    for hx, hy in house:
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        # 가장 가까운 치킨 집 까지의 거리를 더하기
        result += temp
    return result


# 치킨 거리의 합의 최소를 찾아 출력
result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))

print(result)
