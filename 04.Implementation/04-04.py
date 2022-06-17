# 04-04 (게임 개발)
import sys

n, m = map(int, input().split())
a, b, d = map(int, input().split())  # a: 세로 좌표, b: 가로 좌표, d: 방향

mapPosition = []  # 맵 형태를 저장 할 리스트(0: 육지, 1: 바다)
for _ in range(m):
    mapPosition.append(list(map(int, sys.stdin.readline().split())))

passed = [[a, b]]  # 지나간 좌표를 저장 할 리스트(현재 위치 포함)
check = 0  # 확인한 횟수

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
    check += 1

    if mapPosition[A][B] == 1 or [A, B] in passed:  # 확인 후 1(바다)이거나 지나간 좌표 제외
        if check == 4:  # 동,서,남,북 모두 이동 못하는 경우
            a -= ma[d]  # 뒤로 이동
            b -= mb[d]
            check = 0
            if mapPosition[a][b] == 1:  # 뒤로 이동 한 위치가 1(바다)인 경우 종료
                break
        else:
            continue

    else:
        a, b = A, B  # 확인 후 0이면 실제로 이동
        passed.append([a, b])
        check = 0

print(len(passed))
