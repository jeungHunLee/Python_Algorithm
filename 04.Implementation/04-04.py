# 04-04 (게임 개발)
import sys

n, m = map(int, input().split())
a, b, d = map(int, input().split())  # a: 세로 좌표, b: 가로 좌표, d: 방향

mapPosition = []  # 맵 형태를 저장 할 리스트(0: 육지, 1: 바다)
for _ in range(m):
    mapPosition.append(list(map(int, sys.stdin.readline().split())))

passed = [[a, b]]  # 지나간 좌표를 저장 할 리스트(현재 위치 포함)
count = 0  # 확인한 횟수

# 동,서,남,북 방향 정의
ma = [-1, 0, 1, 0]
mb = [0, 1, 0, -1]

# 이동 시작
while True:
    d -= 1  # 방향 회전
    if d == -1:
        d = 3

    A = a + ma[d]  # a좌표 이동
    B = b + mb[d]  # b좌표 이동
    count += 1

    if mapPosition[A][B] == 1 or [A, B] in passed:  # 확인 후 1(바다)이거나 지나간 좌표 제외
        if count == 4:  # 동,서,남,북 모두 이동 못하는 경우
            a -= ma[d]  # 뒤로 이동
            b -= mb[d]
            count = 0
            if mapPosition[a][b] == 1:  # 뒤로 이동 한 위치가 1(바다)인 경우 종료
                break
        else:
            continue

    else:
        a, b = A, B  # 확인 후 0이면 실제로 이동
        passed.append([a, b])
        count = 0

print(len(passed))

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
