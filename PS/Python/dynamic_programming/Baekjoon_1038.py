'''
    제출 언어: Python3
    시간: 76ms
'''
import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())

    answer = -1

    if N <= 9:
        answer = N    

    else:
        dp = [ [0] * 10 for _ in range(10) ]

        for i in range(10):
            dp[0][i] = 1

        cur_num = 9
        cur_row = 1

        while cur_row < 10:
            for i in range(cur_row, 10):
                temp = dp[cur_row-1][i-1] + dp[cur_row][i-1]

                if cur_num + temp >= N:
                    answer = i * (10 ** cur_row) 
                    break

                else:
                    dp[cur_row][i] = temp
                    cur_num += temp
            
            if answer != -1:
                max_num = i

                for i in range(cur_row-1, -1, -1):
                    for j in range(i, max_num):
                        if cur_num + dp[i][j] >= N:
                            max_num = j
                            answer += j * (10 ** i)
                            break

                        else:
                            cur_num += dp[i][j]

                break

            cur_row += 1
    
    print(answer)

