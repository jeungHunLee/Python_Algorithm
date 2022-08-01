# 14-24 (안테나)
n = int(input())
houses = list(map(int, input().split()))

houses.sort()
if n % 2 == 0:
    candidates = [houses[n // 2 - 1], houses[n // 2]]
    distance = 0
    result = []
    for candidate in candidates:
        for house in houses:
            distance += abs(candidate - house)
        result.append(distance)
    print(candidates[result.index(min(result))])
else:
    print(houses[n // 2])