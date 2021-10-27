'''
    제출 언어: Python3
    시간: 3304ms
'''
import sys
from collections import deque

def search():
    global M, N, H, mat, before_cnt, today_list
    dx, dy, dz = [0, 1, 0, -1, 0, 0], [-1, 0, 1, 0, 0, 0], [0, 0, 0, 0, -1, 1]

    go_to_after = 0
    day = 0

    while today_list:
        tomorrow_list = []

        for cr, cc, cz in today_list:
            for i in range(6):
                nr, nc, nz = cr + dy[i], cc + dx[i], cz + dz[i]

                if 0 <= nr < N and 0 <= nc < M and 0 <= nz < H and mat[nr][nc][nz] == 0:
                    go_to_after += 1
                    mat[nr][nc][nz] = 1
                    tomorrow_list.append((nr, nc, nz))

        day += 1
        today_list = tomorrow_list
        
        if before_cnt - go_to_after == 0:
            break

    if before_cnt - go_to_after != 0:
        day = -1

    return day

def solution():
    global before_cnt

    res = -1

    if before_cnt == 0:
        res = 0
    else:
        res = search()

    return res

if __name__ == "__main__":
    M, N, H = map(int, sys.stdin.readline().strip().split())

    mat = [ [ [] for j in range(M) ] for i in range(N) ]

    before_cnt = 0
    today_list = []
    answer = -1

    for i in range(H):
        for j in range(N):
            inputed = list(map(int, sys.stdin.readline().strip().split()))

            for k in range(M):
                mat[j][k].append(inputed[k])

                if inputed[k] == 0:
                    before_cnt += 1
                elif inputed[k] == 1:
                    today_list.append((j, k, i))
    

    answer = solution()
    print(answer)

