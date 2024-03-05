# 16 - 33 (퇴사)
n = int(input())
t, p = [], []

for _ in range(n):
    ti, pi = map(int, input().split())
    t.append(ti)
    p.append(pi)

dp = [0] * (n + 1)
max_value = 0
for i in range(n - 1, -1, -1):
    if i + t[i] <= n:
        max_value = max(max_value, dp[i + t[i]] + p[i])

    dp[i] = max_value

print(max_value)