'''
    제출 언어: Python3
    시간: 120ms
'''
import sys
from collections import deque

def search(sr, sc):
    global M, N, mat, visited, dx, dy

    visited[sr][sc] = True

    que = deque([ (sr, sc) ])
    area = 1

    while que:
        cr, cc = que.popleft()

        for i in range(4):
            nr, nc = cr + dy[i], cc + dx[i]

            if 0 <= nr < M and 0 <= nc < N and mat[nr][nc] == 0 and not visited[nr][nc]:
                area += 1
                visited[nr][nc] = True
                que.append((nr, nc))

    return area


if __name__ == "__main__":
    M, N, K = map(int, sys.stdin.readline().strip().split())

    mat = [ [0] * N for _ in range(M) ]
    visited = [ [False] * N for _ in range(M) ]

    dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]

    answers = []

    for _ in range(K):
        x1, y1, x2, y2 = map(int, sys.stdin.readline().strip().split())
        y1, y2 = M - y1, M - y2
        for i in range(y2, y1):
            for j in range(x1, x2):
                mat[i][j] = 1
    
    for i in range(M):
        for j in range(N):
            if mat[i][j] == 0 and not visited[i][j]:
                answers.append(search(i, j))

    answers.sort()

    print(len(answers))
    print(" ".join(map(str, answers)))

