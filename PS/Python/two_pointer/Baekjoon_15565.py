'''
    제출 언어: Python3
    시간: 524ms
'''
import sys
from collections import deque

if __name__ == "__main__":
    N, K = list(map(int, sys.stdin.readline().strip().split()))

    doll_list = list(map(int, sys.stdin.readline().strip().split()))

    answer = float('inf')
    cur_cnt = 0

    if K == 1:
        if 1 in doll_list:
            answer = 1
        
        else:
            answer = -1
    
    else:
        left, right = 0, 0
        for i in range(N):
            if doll_list[i] == 1:
                left, right = i, i
                break
        
        lion_pos = deque([])

        while right < N:
            if doll_list[right] == 1:
                cur_cnt += 1
                lion_pos.append(right)

                if cur_cnt == K:
                    if answer > right - left + 1:
                        answer = right - left + 1
                    
                    cur_cnt -= 1
                    
                    while lion_pos:
                        np = lion_pos.popleft()

                        if left != np:
                            left = np
                            break
            
            right += 1

        if answer == float('inf'):
            answer = -1

    print(answer)

