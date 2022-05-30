# 모험가 길드
n = input()
data = list(map(int, input().split()))
count = 0   # 그룹에 속한 인원수
result = 0  # 그룹의 개수

for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)