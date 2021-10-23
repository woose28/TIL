'''
    제출 언어: Python3
    시간: 156ms
'''
import sys
from collections import deque

if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().strip().split())

    temp_list = list(map(int, sys.stdin.readline().strip().split()))

    que = deque(temp_list[:K])

    cur_sum = sum(que)
    answer = cur_sum

    for i in range(K, N):
        cur_temp = temp_list[i]
        left_num = que.popleft()
        
        cur_sum = cur_sum - left_num + cur_temp
        que.append(cur_temp)

        answer = max(answer, cur_sum)

    print(answer)

