# 05-03 (특정 거리의 도시 찾기)
from collections import deque
import sys
n, m, k, x = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
count = [0] * (n + 1)  # 도시 간의 거리
answer = []

for _ in range(m):
    t, j = map(int, sys.stdin.readline().split())
    graph[t].append(j)


def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = True
    while queue:
        v = queue.popleft()
        for next in graph[v]:
            if not visited[next]:
                queue.append(next)
                visited[next] = True
                count[next] = count[v] + 1
                if count[next] == k:
                    answer.append(next)
    if len(answer) == 0:
        print(-1)
    else:
        answer.sort()
        for p in answer:
            print(p)


visited = [False] * (n + 1)

bfs(x)
