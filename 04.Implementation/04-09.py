# 04-09 (뱀)
n = int(input())  # 보드의 크기
board = [[0] * n for _ in range(n)]  # 이차원 리스트 보드 생성

k = int(input())  # 사과의 개수
for _ in range(k):
    a, b = map(int, input().split())  # a: 행, b: 열
    board[a - 1][b - 1] = 1

L = int(input())  # 방향 전환 횟수
turn = {}  # 방향 전환
for _ in range(L):
    c, d = input().split()  # c: 초 d: 방향
    turn[int(c)] = d

# 동서남북 정의
mx = [0, 1, 0, -1]
my = [1, 0, -1, 0]

# 이동 시작
head_x, head_y = 0, 0  # 뱀의 머리 좌표
tail_x, tail_y = 0, 0  # 뱀의 꼬리 좌표
board[head_x][head_y] = 2  # 뱀의 현재 위치를 2로 표시
count = 0  # 시간
z = 0  # 진행 방향
info = []  # 이동 경로 정보

while True:
    if count in turn:
        if turn[count] == 'D':
            z += 1
            if z > 3:
                z = 0
        else:
            z -= 1
            if z < 0:
                z = 3

    head_x += mx[z]  # 이동
    head_y += my[z]
    count += 1
    info.append(z)

    if head_x > n - 1 or head_x < 0 or head_y > n - 1 or head_y < 0:  # 머리가 벽을 만나면 종료
        break

    elif board[head_x][head_y] == 1:  # 머리가 사과를 만나면
        board[head_x][head_y] = 2

    elif board[head_x][head_y] == 0:  # 사과가 없는 경우
        board[head_x][head_y] = 2  # 머리는 앞으로 이동
        board[tail_x][tail_y] = 0  # 현재 꼬리 좌표는 0으로 초기화
        w = info.pop(0)
        tail_x += mx[w]
        tail_y += my[w]

    elif board[head_x][head_y] == 2:  # X, Y가 자기 자신과 부딪히면 종료
        break

print(count)

# 예시 답안
n = int(input())
k = int(input())
data = [[0] * (n + 1) for _ in range(n + 1)]  # 맵 정보
info = []  # 방향 회전 정보

# 사과 위치
for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1

# 방향 회전 정보 입력
l = int(input())
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))

# 처음에는 오르쪽을 보고 있으므로(동, 남, 서, 북)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def turn(direction, c):
    if c == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction


def simulate():
    x, y = 1, 1
    data[x][y] = 2  # 뱀이 존재하는 위치는 2
    direction = 0
    time = 0  # 진행 시간
    index = 0  # 다음에 회전할 정보
    q = [(x, y)]  # 뱀이 차지하고 있는 위치 정보
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        # 맵 범위 안에 있고, 뱀의 몸통이 없는 위치라면
        if 1 <= nx <= n and 1 <= ny <= n and data[nx][ny] != 2:
            # 사과가 없다면 이동 후에 꼬리 제거
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                data[px][py] = 0
            # 사과가 있다면 이동 후 꼬리는 그대로
            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx, ny))
        # 벽이나 몸통에 부딪혔다면
        else:
            time += 1
            break
        x, y = nx, ny  # 다음 위치로 머리를 이동
        time += 1
        if index < l and time == info[index][0]:  # 회전할 시간인 경우 회전
            direction = turn(direction, info[index][1])
            index += 1
    return time


print(simulate())
