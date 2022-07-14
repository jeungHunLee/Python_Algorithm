# 05-05 (경쟁적 전염)
from collections import deque

n, k = map(int, input().split())
graph = []  # 지도
for i in range(n):
    graph.append(list(map(int, input().split())))

queue = deque()     # 큐 생성
for num in range(1, k+1):
    for line in range(n):
        if num in graph[line]:
            queue.append([num, line, graph[line].index(num)])   # [바이러스 번호, 행, 열]

s, x, y = map(int, input().split())

# 바이러스에 대하여 방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(s, x, y):
    count = 0
    before = 0  # 이전 바이러스 번호
    now = 0     # 현재 바이러스 번호

    while True:
        if len(queue) == 0:
            break
        v = queue.popleft()
        now = v[0]
        if before == k and now == 1:
            count += 1

        if count == s:
            break

        for i in range(4):
            nx = v[1] + dx[i]
            ny = v[2] + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            else:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = now
                    queue.append([now, nx, ny])
        before = now
    return graph[x - 1][y - 1]


print(bfs(s, x, y))