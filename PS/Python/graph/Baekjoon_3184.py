'''
    제출 언어: Python3
    시간: 208ms
'''
import sys
from collections import deque

def search(sr, sc):
    global R, C, mat, visited, dx, dy

    que = deque([(sr, sc)])
    cur_sheep, cur_wolf = 0, 0

    if mat[sr][sc] == "o":
        cur_sheep += 1
    elif mat[sr][sc] == "v":
        cur_wolf += 1

    while que:
        cr, cc = que.popleft()

        for i in range(4):
            nr, nc = cr + dy[i], cc + dx[i]

            if 0 <= nr < R and 0 <= nc < C and mat[nr][nc] != "#" and not visited[nr][nc]:
                visited[nr][nc] = True

                if mat[nr][nc] == "o":
                    cur_sheep += 1

                elif mat[nr][nc] == "v":
                    cur_wolf += 1
                
                que.append((nr ,nc))
    
    if cur_sheep > cur_wolf:
        cur_wolf = 0
    
    else:
        cur_sheep = 0

    return (cur_sheep, cur_wolf)

if __name__ == "__main__":
    R, C = map(int, sys.stdin.readline().strip().split())

    dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]

    num_sheep, num_wolf = 0, 0

    mat = [ list(sys.stdin.readline().strip()) for _ in range(R) ]
    visited = [ [False] * C for _ in range(R) ]

    for i in range(R):
        for j in range(C):
            if mat[i][j] != "#" and not visited[i][j]:
                visited[i][j] = True
                cur_sheep, cur_wolf = search(i, j)

                num_sheep += cur_sheep
                num_wolf += cur_wolf

    print(num_sheep, num_wolf)

