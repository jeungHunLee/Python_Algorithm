# 모험가 길드
n = input()
data = list(map(int, input().split()))
data.sort()

count = 0   # 그룹에 속한 인원수
result = 0  # 그룹의 개수

for i in data:
    count += 1      # 그룹에 현재 모험가를 포함
    if count >= i:      # 그룹의 인원수가 공포도보다 높거나 같을때 그룹 형성
        result += 1
        count = 0

print(result)