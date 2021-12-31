'''
    제출 언어: Python3
    시간: 120ms
'''
import sys
from collections import deque

def search(n, stones, sp):
    visited = [False] * (n+1)
    visited[sp] = True

    que = deque([ sp ])
    cnt_visit = 1

    while que:
        cp = que.popleft()

        rp = cp + stones[cp-1]
        lp = cp - stones[cp-1]
        
        if 1 <= rp <= n and not visited[rp]:
            visited[rp] = True
            cnt_visit += 1
            que.append(rp)

        if 1 <= lp <= n and not visited[lp]:
            visited[lp] = True
            cnt_visit += 1
            que.append(lp)

    return cnt_visit

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    stones = list(map(int, sys.stdin.readline().strip().split()))
    pos = int(sys.stdin.readline().strip())

    answer = search(n, stones, pos)

    print(answer)

