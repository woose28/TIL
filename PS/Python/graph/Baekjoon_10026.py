'''
    제출 언어: Python3
    시간: 116ms
'''
import sys
from collections import deque

def normal_search(sr, sc, target):
    global N, normal_mat, normal_visited
    dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]

    que = deque([(sr, sc)])

    while que:
        cr, cc = que.popleft()

        for i in range(4):
            nr, nc = cr+dy[i], cc+dx[i]
            
            if 0 <= nr < N and 0 <= nc < N and not normal_visited[nr][nc] and normal_mat[nr][nc] == target:
                normal_visited[nr][nc] = True
                que.append((nr, nc))


def color_search(sr, sc, target):
    global N, color_mat, color_visited
    dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]

    que = deque([(sr, sc)])

    while que:
        cr, cc = que.popleft()

        for i in range(4):
            nr, nc = cr+dy[i], cc+dx[i]

            if 0 <= nr < N and 0 <= nc < N and not color_visited[nr][nc] and color_mat[nr][nc] == target:
                color_visited[nr][nc] = True
                que.append((nr, nc))


if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())

    normal_mat = [ list(sys.stdin.readline().strip()) for _ in range(N) ]
    color_mat = [ [ "R" if e == "G" else e for e in row ] for row in normal_mat ]

    normal_visited = [ [False] * N for _ in range(N) ]
    color_visited= [ [False] * N for _ in range(N) ]

    cnt_normal_part = 0
    cnt_color_part = 0

    for i in range(N):
        for j in range(N):
            if not normal_visited[i][j]:
                normal_visited[i][j] = True
                normal_search(i, j, normal_mat[i][j])
                cnt_normal_part += 1

            if not color_visited[i][j]:
                color_visited[i][j] = True
                color_search(i, j, color_mat[i][j])
                cnt_color_part += 1

    print(cnt_normal_part, cnt_color_part)




