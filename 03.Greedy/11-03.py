# 문자열 뒤집기
# 나의 답안
s = input()
count = 0

for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        count += 1

print((count + 1) // 2)

# 예시 답안
data = input()
count0 = 0  # 전부 0으로 바꾸는 경우
count1 = 0  # 전부 1로 바꾸는 경우

if data[0] == '1':
    count0 += 1     # 0번째 문자가 1이라면, 전부 0으로 만드는 경우의 횟수 +1
else:
    count1 += 1     # 0번째 문자가 0이라면, 전부 1로 만드는 경우의 횟수 +1

for i in range(len(data)-1):
    if data[i] != data[i+1]:
        if data[i+1] == '1':
            count0 += 1     # i에서 i+1로 갈때 문자가 1로 바뀌는 경우, 전부 0으로 만드는 경우의 횟수 +1
        else:
            count1 += 1     # i에서 i+1로 갈때 문자가 0으로 바뀌는 경우, 전부 1로 만드는 경우의 횟수 +1

print(min(count0, count1))