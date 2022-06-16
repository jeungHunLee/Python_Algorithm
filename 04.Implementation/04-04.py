# 04-04 (게임 개발)
import sys

n, m = map(int, input().split())
a, b, head = map(int, input().split())  # a: 세로 좌표, b: 가로 좌표

mapPosition = []
for _ in range(m):
    mapPosition.append(list(map(int, sys.stdin.readline().split())))

currentPosition = [mapPosition[a][b]]

print(currentPosition)