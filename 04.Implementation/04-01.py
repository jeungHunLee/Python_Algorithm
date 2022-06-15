# 04-01 (상하좌우)
# 나의 풀이
n = int(input())
move = input().split()

x, y = 1, 1

for i in range(len(move)):
    if move[i] == 'L':      # 만약 요소가 'L' 이라면
        if y - 1 < 1:       # 범위를 벗어 난다면 무시
            continue
        y -= 1              # y 좌표 1 감소
    elif move[i] == 'R':
        if y + 1 > n:       # 범위를 벗어 난다면 무시
            continue
        y += 1              # y 좌표 1 증가
    elif move[i] == 'U':
        if x - 1 < 1:       # 범위를 벗어 난다면 무시
            continue
        x -= 1              # x 좌표 1 감소
    elif move[i] == 'D':
        if x + 1 > n:       # 범위를 벗어 난다면 무시
            continue
        x += 1              # x 좌표 1 증가

print(x, y)

# 예시 풀이
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    x, y = nx, ny

print(x, y)