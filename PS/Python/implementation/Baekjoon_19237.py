'''
    제출 언어: PyPy3
    시간: 284ms
'''
import sys

def move_shark():
    global N, M, smell_list, shark_info, shark_pri, dx, dy

    keys = list(shark_info.keys())
    keys.sort()

    for shark_id in keys:
        is_moved = False

        cr, cc, cd = shark_info[shark_id]
        cp = shark_pri[shark_id][cd]

        moved_r, moved_c, moved_d = cr, cc, cd

        for nd in cp:
            nr, nc = cr+dx[nd], cc+dy[nd]

            if 0 <= nr < N and 0 <= nc < N and smell_list[nr][nc][0] == 0:
                moved_r, moved_c, moved_d = nr, nc, nd
                is_moved = True
                break 
        
        if not is_moved:
            for nd in cp:
                nr, nc = cr+dx[nd], cc+dy[nd]

                if 0 <= nr < N and 0 <= nc < N and smell_list[nr][nc][0] == shark_id:
                    moved_r, moved_c, moved_d = nr, nc, nd
                    break
        
        shark_info[shark_id] = [moved_r, moved_c, moved_d]

def spread_smell():
    global N, M, K, smell_list, shark_info, left_shark

    keys = list(shark_info.keys())
    keys.sort()

    for shark_id in keys:
        cr, cc, cd = shark_info[shark_id]

        if smell_list[cr][cc][0] == 0 or smell_list[cr][cc][0] == shark_id:
            smell_list[cr][cc] = [shark_id, K+1]
        
        else:
            del shark_info[shark_id]
            left_shark -= 1

def reduce_smell():
    global N, smell_list

    for i in range(N):
        for j in range(N):
            shark_id, total_smell = smell_list[i][j]

            if shark_id == 0:
                continue
            elif total_smell == 1:
                smell_list[i][j] = [0, 0]
            else:
                smell_list[i][j] = [shark_id, total_smell-1]

if __name__ == "__main__":
    N, M, K = map(int, sys.stdin.readline().strip().split())

    smell_list = [ [[0, 0]] * N for _ in range(N) ]
    shark_info = { i: [0, 0, 0] for i in range(1, M+1) }

    for i in range(N):
        pos_info = list(map(int, sys.stdin.readline().strip().split()))
        for j in range(N):
            if pos_info[j] != 0:
                shark_info[pos_info[j]] = [i, j, 0]
                smell_list[i][j] = [pos_info[j], K]
    
    direction_info = [0] + [ d-1 for d in map(int, sys.stdin.readline().strip().split())]

    for i in range(1, M+1):
        cr, cc, _ = shark_info[i]
        shark_info[i] = [cr, cc, direction_info[i]]
    
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    shark_pri = { i: [] for i in range(1, M+1) }

    for i in range(M*4):
        pri = [ d-1 for d in map(int, sys.stdin.readline().strip().split())]
        shark_num = (i // 4) + 1

        shark_pri[shark_num].append(pri)

    answer = -1
    left_shark = M
    T = 0

    while T < 1000:
        T += 1

        move_shark()
        spread_smell()
        reduce_smell()

        if left_shark == 1:
            answer = T
            break
    
    print(answer)
