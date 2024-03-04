# 16 - 31 (금광)
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    data = [[] for _ in range(n)]
    gold = list(map(int, input().split()))

    row = 0
    for i in range(len(gold)):
        data[row].append(gold[i])

        if (i + 1) % m == 0:
            row += 1

    dp = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        dp[i][0] = data[i][0]

    for i in range(m - 1):    # 열
        for j in range(n):    # 행
            # 오른쪽으로 가는 경우
            dp[j][i + 1] = max(dp[j][i] + data[j][i + 1], dp[j][i + 1])

            # 오른쪽 위로 가는 경우
            if 0 < j < n:
                dp[j - 1][i + 1] = max(dp[j - 1][i + 1], dp[j][i] + data[j - 1][i + 1])

            # 오른쪽 아래로 가는 경우
            if j < n - 1:
                dp[j + 1][i + 1] = max(dp[j + 1][i + 1], dp[j][i] + data[j + 1][i + 1])

    result = []
    for i in range(n):
        result.append(dp[i][-1])

    print(max(result))
