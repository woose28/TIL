'''
    제출 언어: Python3
    시간: 424ms
'''
import sys
import heapq

def solution(c1):
    global graph, distance

    distance[c1] = 0
    q = [ (0, c1) ]

    while q:
        cd, cc = heapq.heappop(q)

        if distance[cc] < cd:
            continue

        for nc, w in graph[cc]:
            nd = cd + w

            if distance[nc] > nd:
                distance[nc] = nd
                heapq.heappush(q, (nd, nc))

if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    M = int(sys.stdin.readline().strip())

    graph = [ [] for _ in range(N+1) ]
    distance = [ float('inf') ] * (N+1)

    for _ in range(M):
        s, e, w = map(int, sys.stdin.readline().strip().split())

        graph[s].append((e, w))

    c1, c2 = map(int, sys.stdin.readline().strip().split())

    solution(c1)

    answer = distance[c2]
    
    print(answer)
