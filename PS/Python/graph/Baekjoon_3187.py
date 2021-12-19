'''
    제출 언어: Python3
    시간: 204ms
'''
import sys
from collections import deque

def search(sr, sc):
    global R, C, mat, visited, dx, dy

    num_area_sheep, num_area_wolf =  0, 0

    que = deque([(sr, sc)])
    visited[sr][sc] = True

    while que:
        cr, cc = que.popleft()

        if mat[cr][cc] == 'v':
            num_area_wolf += 1
        elif mat[cr][cc] == 'k':
            num_area_sheep += 1

        for i in range(4):
            nr, nc = cr + dy[i], cc + dx[i]

            if 0 <= nr < R and 0 <= nc < C and mat[nr][nc] != '#' and not visited[nr][nc]:
                visited[nr][nc] = True
                que.append((nr, nc))
    
    if num_area_sheep > num_area_wolf:
        num_area_wolf = 0

    else:
        num_area_sheep = 0

    return (num_area_sheep, num_area_wolf)


if __name__ == "__main__":
    R, C = map(int, sys.stdin.readline().strip().split())

    mat = [ list(sys.stdin.readline().strip()) for _ in range(R) ]

    visited = [ [False] * C for _ in range(R) ]

    dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]

    num_sheep, num_wolf = 0, 0

    for i in range(R):
        for j in range(C):
            if mat[i][j] != '#' and not visited[i][j]:
                num_area_sheep, num_area_wolf = search(i, j)

                num_sheep += num_area_sheep
                num_wolf += num_area_wolf

    print(num_sheep, num_wolf)
