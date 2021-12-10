'''
    제출 언어: Python3
    시간: 944ms
'''
import sys
from collections import deque

def search(sr, sc):
    global M, N, visited, dx, dy

    que = deque([(sr, sc)])

    isSuccess = False

    while que:
        cr, cc = que.popleft()

        for i in range(4):
            nr, nc = cr + dy[i], cc + dx[i]

            if 0 <= nr < M and 0 <= nc < N and mat[nr][nc] == "0" and not visited[nr][nc]:
                if nr == M - 1:
                    isSuccess = True
                    break
                else:    
                    visited[nr][nc] = True
                    que.append((nr, nc))

        if isSuccess:
            break

    return isSuccess

if __name__ == "__main__":
    M, N = map(int, sys.stdin.readline().strip().split())

    mat = [ list(sys.stdin.readline().strip()) for _ in range(M) ]
    
    visited = [ [False] * N for _ in range(M) ]

    dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]

    answer = "NO"

    for i in range(N):
        if mat[0][i] == "0" and not visited[0][i]:
            visited[0][i] = True
            isSuccess = search(0, i)

            if isSuccess:
                answer = "YES"
                break

    print(answer)

