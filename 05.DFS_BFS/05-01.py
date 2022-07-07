# 05-01 (음료수 얼려 먹기)
def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:  # 범위를 벗어나는 경우 제외
        return False

    if graph[x][y] == 0:  # 아직 방문하지 않은 곳 방문 처리
        graph[x][y] = 1
        # 현재 위치에서 상, 하, 좌, 우에 대하여 확인
        dfs(x - 1, y)  # 상
        dfs(x + 1, y)  # 하
        dfs(x, y - 1)  # 좌
        dfs(x, y + 1)  # 우
        return True
    return False


n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            result += 1

print(result)
