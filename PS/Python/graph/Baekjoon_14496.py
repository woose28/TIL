'''
    제출 언어: Python3
    시간: 188ms
'''
import sys
from collections import deque

def search():
    global a, b, mat, visited, answer
    visited[a-1] = True

    que = deque([(a-1, 0)])

    while que:
        w, nr = que.popleft()

        if w == b-1:
            answer = nr
            break

        for  i in range(N):
            if mat[w][i] == 1 and not visited[i]:
                visited[i] = True
                que.append((i, nr+1))


if __name__ == "__main__":
    a, b = map(int, sys.stdin.readline().strip().split())

    N, M = map(int, sys.stdin.readline().strip().split())

    mat = [ [0] * N for _ in range(N) ]
    visited = [False] * N

    for _ in range(M):
        w1, w2 = map(int, sys.stdin.readline().strip().split())

        mat[w1-1][w2-1] = 1
        mat[w2-1][w1-1] = 1

    answer = -1

    search()

    print(answer)
