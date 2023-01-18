# 04-04 (게임 개발)
n, m = map(int, input().split())
x, y, d = map(int, input().split())
board = []
not_visited = [[False for _ in range(m)] for _ in range(n)]    # 방문 여부

for i in range(n):
    row = list(map(int, input().split()))
    board.append(row)
    for j in range(m):
        if row[j] == 0:
            not_visited[i][j] = True
not_visited[x][y] = False    # 현재 위치 방문 처리

# 북, 동, 남, 서 방향에 대한 좌표
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

turn = 0    # 회전 횟수
count = 1    # 방문한 개수
while True:    # 이동 시작
    d -= 1
    if d < 0:
        d = 3
    turn += 1

    nx = x + dx[d]
    ny = y + dy[d]

    if 0 <= nx < n and 0 <= ny < m:
        if not_visited[nx][ny]:
            x = nx
            y = ny
            not_visited[x][y] = False
            turn = 0
            count += 1

    if turn == 4:    # 네 방향 모두 확인 했다면 뒤로 이동
        x -= dx[d]
        y -= dy[d]
        if board[x][y] == 1:    # 뒤가 바다면 이동 종료
            break
        turn = 0

print(count)

#  예시 답안
n, m = int(input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]
# 현재 캐릭터의 X좌표, Y좌표 방향을 입력하기
x, y, direction = map(int, input().split())
d[x][y] = 1  # 현재 위치 방문 처리

# 전제 맵 정보 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 서, 남 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


# 이동 시작
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1

    # 네방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀 있는 경우
        else:
            break
        turn_time = 0

print(count)
