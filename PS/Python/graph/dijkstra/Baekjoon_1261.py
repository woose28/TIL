'''
    제출 언어: Python3
    시간: 100ms
'''
import sys
import heapq

def solution():
    global N, M, mat

    cnt_wall_mat = [ [ float('inf' ) ] * M for _ in range(N) ]
    dx, dy = (0, 1, 0, -1), (-1, 0, 1, 0)

    cnt_wall_mat[0][0] = 0

    heap = [(0, 0, 0)] # (cnt_wall, r, c)
    heapq.heapify(heap)

    res = 0

    while heap:
        cw, cr, cc = heapq.heappop(heap)

        for i in range(4):
            nr, nc = cr+dy[i], cc+dx[i]

            if 0 <= nr < N and 0 <= nc < M:
                if mat[nr][nc] == 0 and cw < cnt_wall_mat[nr][nc]:
                    cnt_wall_mat[nr][nc] = cw
                    heapq.heappush(heap, (cw, nr, nc))

                elif mat[nr][nc] == 1 and cw+1 < cnt_wall_mat[nr][nc]:
                    cnt_wall_mat[nr][nc] = cw+1
                    heapq.heappush(heap, (cw+1, nr, nc))
    
    res = cnt_wall_mat[N-1][M-1]

    return res
    

if __name__ == "__main__":
    M, N = map(int, sys.stdin.readline().strip().split())

    mat = [ list(map(int, sys.stdin.readline().strip())) for _ in range(N) ]

    answer = solution()

    print(answer)
