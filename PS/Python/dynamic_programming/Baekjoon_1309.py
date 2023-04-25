N = int(input())

dp = [ [0] * 3 for _ in range(N) ]

dp[0] = [1, 1, 1]

for i in range(1, N):
  dp[i] = [(dp[i - 1][1] + dp[i - 1][2]) % 9901, (dp[i - 1][0] + dp[i - 1][2]) % 9901, sum(dp[i - 1]) % 9901]

print((dp[N - 1][0] + dp[N - 1][1] + dp[N - 1][2]) % 9901)
