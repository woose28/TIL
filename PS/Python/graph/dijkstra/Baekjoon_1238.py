'''
    제출 언어: Python3
    시간: 1296ms
'''
import sys
import heapq

def search_graph(sv):
    global N, graph

    distance = [ float("inf") ] * N
    distance[sv] = 0

    que = [ (0, sv) ]

    while que:
        cw, cv = heapq.heappop(que)

        if cw > distance[cv]:
            continue

        for w, nv in graph[cv]:
            nw = cw + w

            if nw < distance[nv]:
                distance[nv] = nw
                heapq.heappush(que, (nw, nv))
    
    return distance

if __name__ == "__main__":
    N, M, X = map(int, sys.stdin.readline().strip().split())

    graph = [ [] for _ in range(N) ]

    for _ in range(M):
        ls, le, lw = map(int, sys.stdin.readline().strip().split())

        ls, le = ls - 1, le - 1
        graph[ls].append((lw, le))

    X -= 1

    e_to_s = search_graph(X)

    answer = 0

    for i in range(N):
        s_to_e = search_graph(i)

        answer = max(answer, e_to_s[i]+s_to_e[X])

    print(answer)

