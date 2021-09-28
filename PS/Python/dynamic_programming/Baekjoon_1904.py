'''
    제출 언어: Python3
    시간: 368ms 
'''
import sys

def solution():
    global N, dp

    dp[1] = 1
    dp[2] = 2

    for i in range(3, N+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 15746
    
if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    dp = [0] * (N+1)

    answer = None

    if N == 1:
        answer = 1

    elif N == 2:
        answer = 2

    else:
        solution()
        answer = dp[N]

    print(answer)

