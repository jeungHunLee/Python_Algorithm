# 05-08 (감시 피하기)
from itertools import combinations

n = int(input())
board = []
teachers = []
spaces = []

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        if board[i][j] == 'T':
            teachers.append([i, j])
        elif board[i][j] == 'X':
            spaces.append([i, j])

# 특정 방향으로 감시 진행
def watch(x, y, direction):
    # 왼쪽 방향 감시
    if direction == 0:
        while y >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y -= 1
    # 오른쪽 방향 감시
    if direction == 1:
        while y < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y += 1
    # 위쪽 방향으로 감시
    if direction == 2:
        while x >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x -= 1
    # 아래 방향으로 감시
    if direction == 3:
        while x < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x += 1

def process():
    # 선생님의 위치를 하나씩 확인
    for x, y in teachers:
        for i in range(4):
            if watch(x, y, i):
                return True
        return False

find = False

# 빈 공간에서 3개를 뽑는 모든 조합 확인
for data in combinations(spaces, 3):
    for x, y in data:
        board[x][y] = 'O'

    if not process():
        find = True
        break

    for x, y in data:
        board[x][y] = 'X'

if find:
    print("YES")
else:
    print("NO")