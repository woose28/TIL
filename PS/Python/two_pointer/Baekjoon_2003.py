'''
    제출언어: Python3
    시간: 96ms
'''
import sys
from collections import deque

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().strip().split())

    num_list = list(map(int, sys.stdin.readline().strip().split()))

    que = deque([0])
    sum_que = 0
    answer = 0

    for i in range(N):
        cur_num = num_list[i]

        if sum_que + cur_num <= M:
            if sum_que + cur_num == M:
                answer += 1
            que.append(cur_num)
            sum_que += cur_num

        else:
            for _ in range(len(que)):
                left_num = que.popleft()

                sum_que -= left_num

                if sum_que + cur_num <= M:
                    if sum_que + cur_num == M:
                        answer += 1
                    que.append(cur_num)
                    sum_que += cur_num

                    break
    

    print(answer)
