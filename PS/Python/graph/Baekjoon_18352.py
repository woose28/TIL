'''
    제출 언어: Python3
    시간: 2756ms
'''
import sys
from collections import deque

def search():
    global N, X, graph, distance

    que = deque([ (X-1, 0) ])
    distance[X-1] = 0

    while que:
        cn, cd = que.popleft()
    
        if cd <= distance[cn]:
            for nn in graph[cn]:
                if cd + 1 <= distance[nn]:
                    distance[nn] = cd + 1
                    que.append((nn, cd + 1))

if __name__ == "__main__":
    N, M, K, X = map(int, sys.stdin.readline().strip().split())

    graph = [ [] * N for _ in range(N) ]

    for _ in range(M):
        r, c = map(int, sys.stdin.readline().strip().split())
        graph[r-1].append(c-1)

    distance = [ float('inf') ] * N

    search()

    candidates = []

    for nn in range(N):
        if distance[nn] == K:
            candidates.append(str(nn+1))
    
    if len(candidates) == 0:
        print(-1)
    else:
        print("\n".join(candidates))

