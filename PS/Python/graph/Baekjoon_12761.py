'''
    제출 언어: Python3
    시간: 360ms
'''
import sys
from collections import deque

def find_next_pos(cur_pos, index):
    global A, B

    if index == 0:
        return  cur_pos + 1
    elif index == 1:
        return cur_pos + A
    elif index == 2:
        return cur_pos + B
    elif index == 3:
        return cur_pos * A
    elif index == 4:
        return cur_pos * B
    elif index == 5:
        return  cur_pos - 1
    elif index == 6:
        return cur_pos - A
    elif index == 7:
        return cur_pos - B

def solution():
    global A, B, N, M

    que = deque([(N, 0)])
    result = 0

    MIN_NUM = 0
    MAX_NUM = 100000

    visited = [ False ] * (MAX_NUM+1)
    visited[N] = True

    while que:
        cp, ct = que.popleft()

        if cp == M:
            result = ct
            break

        for i in range(8):
            np = find_next_pos(cp, i)

            if MIN_NUM <= np <= MAX_NUM and not visited[np]:
                visited[np] = True
                que.append((np, ct + 1))
    
    return result


if __name__ == "__main__":
    A, B, N, M = map(int, sys.stdin.readline().strip().split())

    answer = solution()

    print(answer)
