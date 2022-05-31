# 문자열 뒤집기
s = input()
count = 0

for i in range(len(s) - 1):
    if s[i] == s[i+1]:
        continue
    else:
        count += 1  # 문자열이 다르면 구분

result = (count + 1) // 2   # 처음과 끝이 다른 경우를 위하여 count에 1을 더하기
print(result)