# 05-04 (연구소)
from itertools import combinations
import copy

n, m = map(int, input().split())
board = []  # 맵
blank = []  # 빈칸의 좌표
virus = []  # 바이러스 좌표

for i in range(n):
    board.append(list(map(int, input().split())))
    for j in range(m):
        if board[i][j] == 0:
            blank.append([i, j])
        elif board[i][j] == 2:
            virus.append([i, j])

candidates = list(combinations(blank, 3))  # 벽을 세울 조합


def safeZone(candidate):
    for element in candidate:
        new_board[element[0]][element[1]] = 1  # 벽 세우기

    # 바이러스 확산
    for element in virus:
        dfs(element[0], element[1])     # DFS 탐색 사용

    count = 0  # 안전 영역의 크기
    for i in range(n):
        count += new_board[i].count(0)
    return count


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return

    if new_board[x][y] == 2 or new_board[x][y] == 0:
        new_board[x][y] = 1
        dfs(x - 1, y)   # 상
        dfs(x + 1, y)   # 하
        dfs(x, y - 1)   # 좌
        dfs(x, y + 1)   # 우
        return
    return


result = 0
for candidate in candidates:
    new_board = copy.deepcopy(board)
    result = max(result, safeZone(candidate))

print(result)