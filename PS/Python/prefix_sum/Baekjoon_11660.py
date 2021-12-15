'''
    제출 언어: Python3
    시간: 1196ms
'''
import sys

def init():
    global N, mat, dp

    for i in range(1, N+1):
        for j in range(1, N+1):
            dp[i][j] = dp[i][j-1] + mat[i-1][j-1]

    for i in range(1, N+1):
        for j in range(1, N+1):
            dp[i][j] += dp[i-1][j]
    
    
if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().strip().split())

    mat = [ list(map(int, sys.stdin.readline().strip().split())) for _ in range(N) ]

    dp = [ [0] * (N+1) for _ in range(N+1) ]
    
    init()

    for _ in range(M):
        x1, y1, x2, y2 = map(int, sys.stdin.readline().strip().split())

        print(dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1])
    
