import sys

N = int(sys.stdin.readline())
mat = [ [ int(char) for char in sys.stdin.readline().split(' ')] for _ in range(N) ]

dp = [ [ [0] * 3 for _ in range(N) ] for _ in range(N)]

dp[0][1][0] = 1

for i in range(2, N):
  for j in range(0, i):
    if mat[j][i] == 1:
      continue
    
    if i - 1 >= 0 and mat[j][i - 1] == 0:
      dp[j][i][0] = dp[j][i - 1][0] + dp[j][i - 1][2]

    if j - 1 >= 0 and mat[j - 1][i] == 0:
      dp[j][i][1] = dp[j - 1][i][1] + dp[j - 1][i][2]
    
    if i - 1 >= 0 and mat[j][i - 1] == 0 and j - 1 >= 0 and mat[j - 1][i] == 0:
      dp[j][i][2] = sum(dp[j - 1][i - 1])
    
  for j in range(0, i + 1):
    if mat[i][j] == 1:
      continue

    if j - 1 >= 0 and mat[i][j - 1] == 0:
      dp[i][j][0] = dp[i][j - 1][0] + dp[i][j - 1][2]

    if i - 1 > 0 and mat[i - 1][j] == 0:
      dp[i][j][1] = dp[i - 1][j][1] + dp[i - 1][j][2]
    
    if j - 1 >= 0 and mat[i][j - 1] == 0 and i - 1 > 0 and mat[i - 1][j] == 0:
      dp[i][j][2] = sum(dp[i - 1][j - 1])


print(sum(dp[N - 1][N - 1]))
