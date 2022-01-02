'''
    제출 언어: Python3
    시간: 100ms
'''
import sys
from collections import deque

def search(sr, sc):
    global mat, answer_list

    que = deque([(sr, sc, mat[sr][sc])])
    num_list = []

    while que:
        cr, cc, cs = que.popleft()

        if len(cs) == 6:
            answer_list.add(cs)
            continue
        
        for i in range(4):
            nr, nc = cr + dy[i], cc + dx[i]

            if 0 <= nr < 5 and 0 <= nc < 5:
                que.append((nr, nc, cs+mat[nr][nc]))
    
    return num_list


if __name__ == "__main__":
    mat = [ list(sys.stdin.readline().strip().split()) for _ in range(5) ]
    dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]
    
    answer_list = set()

    for i in range(5):
        for j in range(5):
            search(i, j)

    
    answer = len(answer_list)
    print(answer)
