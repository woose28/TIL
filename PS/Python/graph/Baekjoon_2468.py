'''
    제출 언어: Python3
    시간: 1464ms
'''
import sys
from collections import deque

def search(sr, sc, rain):
    global N, mat, visited, dx, dy

    que = deque([(sr, sc)])

    while que:
        cr, cc = que.popleft()
        
        for i in range(4):
            nr, nc = cr+dy[i], cc+dx[i]

            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and mat[nr][nc] > rain:
                visited[nr][nc] = True
                que.append((nr, nc))
    

if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())

    info = []
    mat = []

    for i in range(N):
        row = list(map(int, sys.stdin.readline().strip().split()))

        info.extend(row)
        mat.append(row)

    info = list(set(info))
    info.sort()

    dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]

    answer = 1

    for rain in info:

        visited = [ [False] * N for _ in range(N) ]
        cnt_safe_zone = 0

        for i in range(N):
            for j in range(N):
                if mat[i][j] > rain and not visited[i][j]:
                    cnt_safe_zone += 1
                    visited[i][j] = True
                    search(i, j, rain)

        answer = max(answer, cnt_safe_zone)
    
    print(answer)
