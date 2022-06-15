# 04-02 (시각)
n = int(input())
count = 0

for i in range(n + 1):      # 시간
    for j in range(60):         # 분
        for k in range(60):         # 초
            if '3' in str(i) + str(j) + str(k):     # 3이 존재 하는지 확인
                count += 1
print(count)