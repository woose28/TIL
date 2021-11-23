'''
    제출 언어: Python3
    시간: 324ms
'''
import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())

    num_list = list(map(int, sys.stdin.readline().strip().split()))
    dp = [0] * (N + 1)

    M = int(sys.stdin.readline().strip())

    answers = []

    for i in range(1, N+1):
        dp[i] = dp[i-1]+ num_list[i-1]
    
    for _ in range(M):
        i, j = map(int, sys.stdin.readline().strip().split())

        answers.append(dp[j]-dp[i-1])
    
    for answer in answers:
        print(answer)
    