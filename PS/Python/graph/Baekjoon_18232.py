'''
    제출 언어: Python3
    시간: 1488ms
'''
import sys
from collections import deque

def search():
    global N, M, S, E, port

    que = deque([(S, 0)])
    visited = [ False ] * (N+1) 

    turn = 0

    while que:
        cp, ct = que.popleft()

        if cp == E:
            turn = ct
            break
        
        for i in range(3):
            if i == 0:
                np = cp + 1

                if 1 <= np <= N and not visited[np]:
                    visited[np] = True
                    que.append((np, ct+1))

            elif i == 1:
                np = cp - 1
                
                if 1 <= np <= N and not visited[np]:
                    visited[np] = True
                    que.append((np, ct+1))

            elif cp in port:
                for np in port[cp]:
                    if 1 <= np <= N and not visited[np]:
                        visited[np] = True
                        que.append((np, ct+1))

    return turn    

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().strip().split())
    S, E = map(int, sys.stdin.readline().strip().split())

    port = {}

    for _ in range(M):
        x, y = map(int, sys.stdin.readline().strip().split())

        if x in port:
            port[x].append(y)
        
        else:
            port[x] = [y]

        if y in port:
            port[y].append(x)

        else:
            port[y] = [x]
    

    answer = search()

    print(answer)
