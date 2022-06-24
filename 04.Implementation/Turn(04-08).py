# 정사각형 모양의 행렬 90도 회전
def turn(before):
    n = len(before)  # 행의 길이
    after = [[0] * n for _ in range(n)]  # 회전한 2차원 배열을 저장할 배열

    for a in range(n):  # 행의 위치
        for b in range(n):  # 열의 위치
            after[b][n - 1 - a] = before[a][b]

    return after


test = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(turn(test))  # [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
