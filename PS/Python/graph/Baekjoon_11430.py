'''
    제출 언어: Python3
    시간: 172ms
'''
import sys
from collections import deque

def search(cur_idx):
    global N, graph, connection_mat

    visited = [False] * N

    que = deque([ cur_idx ])

    while que:
        cur_node = que.popleft()

        for next_node in range(N):
            if graph[cur_node][next_node] == 1 and not visited[next_node]:
                visited[next_node] = True
                que.append(next_node)

    for i in range(N):
        if visited[i]:
            connection_mat[cur_idx][i] = "1"

if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())

    graph = [ list(map(int, sys.stdin.readline().strip().split())) for _ in range(N) ]
    connection_mat = [ ["0"] * N for _ in range(N) ]

    for i in range(N):
        search(i)
    
    for row in connection_mat:
        print(" ".join(row))