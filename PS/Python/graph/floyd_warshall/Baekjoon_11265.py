'''
    제출 언어: Python3
    시간: 5124ms
'''
import sys
import heapq

def compute_optimal_distance():
    global N, graph

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
    
    

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().strip().split())

    graph = [ list(map(int, sys.stdin.readline().strip().split())) for _ in range(N) ]

    service_list = [ list(map(int, sys.stdin.readline().strip().split())) for _ in range(M) ]

    compute_optimal_distance()

    for A, B, C in service_list:
        if graph[A-1][B-1] <= C:
            print('Enjoy other party')
        
        else:
            print('Stay here')


