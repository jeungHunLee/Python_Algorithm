# fibonacci sequence with recursion(Top-Down)
dp = [0] * 100

def fibonacci(n):
    if n == 1 or n == 2:
        return 1

    if dp[n] != 0:
        return dp[n]

    dp[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return dp[n]

print(fibonacci(6))    # 8

# fibonacci sequence with for(Bottom-Down)
fibonacci = [0] * 100
fibonacci[1] = fibonacci[2] = 1

for i in range(3, 100):
    fibonacci[i] = fibonacci[i - 1] + fibonacci[i - 2]

print(fibonacci[6])    # 8
