'''
    제출 언어: Python3
    시간: 340ms
'''
import sys

if __name__ == "__main__":
    n, k = map(int, sys.stdin.readline().strip().split())
    coins = []

    for _ in range(n):
        coins.append(int(sys.stdin.readline().strip()))

    dp = [ 0 ] * (k+1)
    dp[0] = 1

    for c in coins:
        for i in range(1, k+1):
            if i - c >= 0:
                dp[i] += dp[i-c]
    
    answer = dp[k]
    print(dp[k])

