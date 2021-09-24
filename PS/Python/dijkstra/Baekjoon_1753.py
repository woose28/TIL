'''
    제출 언어: Python3
    시간: 864ms
'''
import heapq
import sys

def solution():
    global graph, distance, K

    q = [ (0, K) ]
    distance[K] = 0

    while q:
        cd, cn = heapq.heappop(q)

        if distance[cn] < cd:
            continue

        for nn, d in graph[cn]:
            nd = cd+d

            if nd < distance[nn]:
                distance[nn] = nd
                heapq.heappush(q, (nd, nn))
    

if __name__ == "__main__":
    V, E = map(int, sys.stdin.readline().strip().split())
    K = int(sys.stdin.readline().strip())

    graph = [ [] for _ in range(V+1) ]
    distance = [ float('inf') for _ in range(V+1) ]

    for _ in range(E):
        u, v, w = map(int, sys.stdin.readline().strip().split())

        graph[u].append((v, w))


    solution()

    for i in range(1, V+1):
        if distance[i] == float('inf'):
            print("INF")
        else:
            print(distance[i])
    
