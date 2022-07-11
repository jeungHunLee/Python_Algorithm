from collections import deque


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True   # 시작 노드 방문처리
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


graph = [
    [],
    [2, 3],
    [1, 4, 5],
    [1, 6],
    [2, 5],
    [2, 4],
    [3]
]

visited = [False] * 7

bfs(graph, 1, visited)      # 1 2 3 4 5 6
