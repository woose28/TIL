'''
    제출 언어: Python3
    시간: 168ms
'''
import sys

def accumulate():
    global N, M, mat, dp

    for i in range(1, N+1):
        for j in range(1, M+1):
            dp[i][j] = mat[i-1][j-1] + dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1]


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().strip().split())
    mat = [ list(map(int, sys.stdin.readline().strip().split())) for _ in range(N) ]
    K = int(sys.stdin.readline().strip())
    part_list = [ list(map(int, sys.stdin.readline().strip().split())) for _ in range(K)]

    dp = [ [0] * (M+1) for _ in range(N+1) ]
    
    accumulate()

    for part in part_list:
        i, j, x, y = part

        print(dp[x][y] - dp[i-1][y] - dp[x][j-1] + dp[i-1][j-1])
    