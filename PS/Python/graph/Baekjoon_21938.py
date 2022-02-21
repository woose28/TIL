'''
    제출 언어: Python3
    시간: 1268ms
'''
import sys
from collections import deque

def search(i, j):
    global N, mat, visited, dx, dy

    que = deque([(i, j)])

    while que:
        cr, cc = que.popleft()

        for i in range(4):
            nr, nc = cr + dy[i], cc + dx[i]

            if 0 <= nr < N and 0 <= nc < M and mat[nr][nc] == 255 and not visited[nr][nc]:
                visited[nr][nc] = True
                que.append((nr, nc))
    


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().strip().split())

    mat = []

    for i in range(N):
        row = []

        row_input = list(map(int, sys.stdin.readline().strip().split()))

        for j in range(0, M*3, 3):
            row.append(sum(row_input[j: j+3]))
        

        mat.append(row)
    
    T = int(sys.stdin.readline().strip()) *  3


    for i in range(N):
        for j in range(M):
            if mat[i][j] >= T:
                mat[i][j] = 255
            else:
                mat[i][j] = 0

    visited = [ [False] * M for _ in range(N) ]
    dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]

    answer = 0

    for i in range(N):
        for j in range(M):
            if mat[i][j] == 255 and not visited[i][j]:
                answer += 1
                visited[i][j] = True
                search(i, j)

    print(answer)
    