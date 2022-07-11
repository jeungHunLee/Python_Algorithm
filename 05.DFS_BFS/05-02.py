# 05-02 (미로 탈출)
from collections import deque
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
dx = [0, 1]     # 하, 우 이동
dy = [1, 0]     # 하, 우 이동


def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    while queue:
        x, y = queue.popleft()
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= n or ny >= m:
                continue
            elif graph[nx][ny] == 0:
                continue
            else:
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx, ny])

    return graph[n-1][m-1]


print(bfs(0, 0))


