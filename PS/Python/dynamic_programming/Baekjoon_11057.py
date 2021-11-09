'''
    제출 언어: Python3
    시간: 68ms
'''
import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())

    dp = [ 1 ] * 10

    for _ in range(N-1):
        cur = [0] * 10
        cur[0] = 1
        cur[1] = (dp[0]+dp[1]) % 10007
        
        for i in range(2, 10):
            cur[i] = (cur[i-1] + dp[i]) % 10007

        dp = cur
    
    answer = 0

    for i in dp:
        answer = (answer + i) % 10007

    print(answer)