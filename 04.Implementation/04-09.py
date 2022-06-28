# 04-09 (뱀)
import sys

n = int(input())  # 보드의 크기
board = [[0] * n for _ in range(n)]  # 이차원 리스트 보드 생성

k = int(input())  # 사과의 개수
for _ in range(k):
    a, b = map(int, sys.stdin.readline().split())  # a: 행, b: 열
    board[a - 1][b - 1] = 1

L = int(input())  # 방향 전환 횟수
turn = {}  # 방향 전환
for _ in range(L):
    c, d = sys.stdin.readline().split()  # c: 초 d: 방향
    turn[int(c)] = d

# 동서남북 정의
mx = [0, 1, 0, -1]
my = [1, 0, -1, 0]

# 이동 시작
head_x, head_y = 0, 0  # 뱀의 머리 좌표
tail_x, tail_y = 0, 0  # 뱀의 꼬리 좌표
board[head_x][head_y] = 2  # 현재 위치를 2로 표시
count = 0  # 시간
z = 0  # 진행 방향
move = []   # 이동 경로 저장

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
    move.append(z)

    if head_x > n - 1 or head_x < 0 or head_y > n - 1 or head_y < 0:  # 머리가 벽을 만나면 종료
        break

    elif board[head_x][head_y] == 1:  # 머리가 사과를 만나면
        board[head_x][head_y] = 2

    elif board[head_x][head_y] == 0:  # 사과가 없는 경우
        board[head_x][head_y] = 2   # 머리는 앞으로 이동
        board[tail_x][tail_y] = 0   # 현재 꼬리 좌표는 0으로 초기화
        w = move.pop(0)
        tail_x += mx[w]
        tail_y += my[w]

    elif board[head_x][head_y] == 2:  # X, Y가 자기 자신과 부딪히면 종료
        break

print(count)
