# 숫자 카드 게임
n, m = map(int, input().split())
min_data = []

for _ in range(n):  # 행의 길이 만큼 데이터 입력 받기
    data = list(map(int, input().split()))
    min_data.append(min(data))  # 각 행의 최솟값 찾기

print(max(min_data))  # 각 행의 최솟값 중 최댓값 출력
