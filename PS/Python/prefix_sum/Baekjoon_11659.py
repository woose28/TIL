'''
    제출 언어: Python3
    시간: 344ms
'''
import sys

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().strip().split())

    num_list = list(map(int, sys.stdin.readline().strip().split()))
    section_list = [ list(map(int, sys.stdin.readline().strip().split())) for _ in range(M) ]

    dp = [0] * (N+1)

    for i in range(1, N+1):
        dp[i] = num_list[i-1] + dp[i-1]
    
    for i, j in section_list:
        print(dp[j]-dp[i-1])
    
