'''
    제출 언어: Python3
    시간: 168ms
'''
import sys
from collections import deque

def move_air(sr, sc):
    global N, M, mat, dx, dy

    que = deque([(sr, sc)])
    mat[sr][sc] = -1

    while que:
        cr, cc = que.popleft()

        for i in range(4):
            nr, nc = cr + dy[i], cc + dx[i]

            if 0 <= nr < N and 0 <= nc < M and mat[nr][nc] == 0:
                mat[nr][nc] = -1
                que.append((nr, nc))

def melt():
    global N, M, mat, dx, dy

    cnt_melted = 0

    for i in range(N):
        for j in range(M):
            if mat[i][j] == 1:
                for k in range(4):
                    nr, nc = i + dy[k], j + dx[k]

                    if 0 <= nr < N and 0 <= nc < M and mat[nr][nc] == -1:
                        mat[i][j] = 2
                        break
    
    for i in range(N):
        for j in range(M):
            if mat[i][j] == 2:
                mat[i][j] = -1
                cnt_melted += 1

    return cnt_melted

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().strip().split())

    mat = [ list(map(int, sys.stdin.readline().strip().split())) for _ in range(N) ]

    dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]

    cur_time = 0
    cnt_cur_cheese = 0

    for i in range(N):
        for j in range(M):
            if mat[i][j] == 1:
                cnt_cur_cheese += 1

    cnt_prev_cheese = cnt_cur_cheese

    move_air(0, 0)

    while cnt_cur_cheese > 0:
        for i in range(N):
            for j in range(M):
                if mat[i][j] == -1:
                    for k in range(4):
                        nr, nc = i+dy[k], j+dx[k]

                        if 0 <= nr < N and 0 <= nc < M and mat[nr][nc] == 0:
                            move_air(nr, nc)
        
        cnt_melted = melt()

        cnt_prev_cheese = cnt_cur_cheese
        cnt_cur_cheese -= cnt_melted
        cur_time += 1

    print(cur_time)
    print(cnt_prev_cheese)


