'''
    제출 언어: Python3
    시간: 144ms
'''
import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    num_list = list(map(int, sys.stdin.readline().strip().split()))

    dp = [1] * N

    for i in range(N-2, -1, -1):
        cur_num = num_list[i]

        for j in range(i+1, N):
            if cur_num > num_list[j]:
                if dp[i] <= dp[j]:
                    dp[i] = dp[j] + 1

    answer = max(dp)

    print(answer)
    