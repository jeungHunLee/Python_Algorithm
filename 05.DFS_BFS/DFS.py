# DFS 예제
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


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

dfs(graph, 1, visited)      # 1 2 4 5 3 6