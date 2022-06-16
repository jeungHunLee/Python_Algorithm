# 04-03 (왕실의 나이트)
currentPosition = input()   # 현재 위치
x = ord(currentPosition[0])     # x 좌표는 현재 위치의 첫번째 문자
y = int(currentPosition[1])     # y 좌표는 현재 위치의 두번째 문자
count = 0
# 이동 가능한 경우의 수
move = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]

for i in range(len(move)):
    next_x = x + move[i][0]
    next_y = y + move[i][1]

    if next_x < 97 or next_x > 104 or next_y < 1 or next_y > 8:     # 범위를 벗어 나는 좌표 무시
        continue

    count += 1

print(count)