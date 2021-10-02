'''
    제출 언어: Python3
    시간: 1140ms
'''
import sys

if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())

    answer = []

    for _ in range(T):
        n = int(sys.stdin.readline().strip())

        score_list = []

        for _ in range(2):
            scores = list(map(int, sys.stdin.readline().strip().split()))

            score_list.append(scores)
        
        cnt_col = len(score_list[0])
        dp = [0, score_list[0][0], score_list[1][0]]

        for i in range(1, cnt_col):
            temp1 = max(dp[0], dp[1], dp[2])
            temp2 = max(dp[0]+score_list[0][i], dp[2]+score_list[0][i])
            temp3 = max(dp[0]+score_list[1][i], dp[1]+score_list[1][i])

            dp[0] = temp1
            dp[1] = temp2
            dp[2] = temp3

        max_score = max(dp)
        answer.append(max_score)
    
    for res in answer:
        print(res)
    