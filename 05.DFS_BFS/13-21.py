from collections import deque

n, l, r = map(int, input().split())
data = []

for _ in range(n):
    data.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
isTrue = True
cnt = 0

while True:
    visited = [[False] * n for _ in range(n)]
    group = [[0] * n for _ in range(n)]
    isTrue = False
    for a in range(n):
        for b in range(n):
            if not visited[a][b]:
                q = deque([(a, b)])
                indexes = [(a, b)]
                total = data[a][b]
                while q:
                    x, y = q.popleft()
                    visited[x][y] = True

                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]

                        if nx < 0 or ny < 0 or nx >= n or ny >= n:
                            continue

                        if not visited[nx][ny] and l <= abs(data[x][y] - data[nx][ny]) <= r:
                            q.append((nx, ny))
                            visited[nx][ny] = True
                            indexes.append((nx, ny))
                            total += data[nx][ny]

                if len(indexes) > 1: isTrue = True

                for x, y in indexes:
                    data[x][y] = total // len(indexes)

    if not isTrue:
        break

    cnt += 1

print(cnt)