import sys

N = int(sys.stdin.readline().strip())
soldiers = list(map(int, sys.stdin.readline().strip().split(' ')))

dp = [ 0 for _ in range(N) ]

dp[0] = 1

for i in range(N):
  greatestSoldiersCount = 0

  for j in range(i - 1, -1, -1):
    if soldiers[i] < soldiers[j] and greatestSoldiersCount < dp[j]:
      greatestSoldiersCount = dp[j]

  dp[i] = greatestSoldiersCount + 1


print(N - max(dp))
