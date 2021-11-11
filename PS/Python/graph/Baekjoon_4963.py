'''
    제출 언어: Python3
    시간: 116ms
'''
import sys
from collections import deque

def search(i, j, visited):
    global w, h, mat
    que = deque([(i, j)])
    dx, dy = [0, 1, 1, 1, 0, -1, -1, -1], [-1, -1, 0, 1, 1, 1, 0, -1]

    while que:
        cr, cc = que.popleft()

        for i in range(8):
            nr, nc = cr+dy[i], cc+dx[i]

            if 0 <= nr < h and 0 <= nc < w and mat[nr][nc] == 1 and not visited[nr][nc] :
                visited[nr][nc] = True
                que.append((nr, nc))
            
        
    

if __name__ == "__main__":
    answers = []

    while True:
        w, h = list(map(int, sys.stdin.readline().strip().split()))

        if w == 0 and h == 0:
            break

        mat = [ list(map(int, sys.stdin.readline().strip().split())) for _ in range(h) ]

        cnt_island = 0

        visited = [ [ False ] * w for _ in range(h) ]

        for i in range(h):
            for j in range(w):
                if mat[i][j] == 1 and not visited[i][j]:
                    visited[i][j] = True
                    search(i, j, visited)
                    cnt_island += 1

        answers.append(str(cnt_island))
    
    print("\n".join(answers))

