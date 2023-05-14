import sys

K, P, N = map(int, sys.stdin.readline().split(' '))

def solution(K, P, N):
    dp = {}

    def recursion(n):
        if n == 1:
            return P

        elif n in dp:
            return dp[n]
        
        elif n % 2 == 0:
            dp[n] = (recursion(n // 2) * recursion(n // 2)) % 1000000007
            return dp[n]
        
        else:
            dp[n] = (recursion(n // 2) * recursion(n // 2) * P) % 1000000007
            return dp[n]
        
    answer = (K * recursion(N * 10)) % 1000000007
    
    print(answer)


solution(K, P, N)