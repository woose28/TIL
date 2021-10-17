'''
    제출 언어: PyPy3
    시간: 248ms
'''
import sys

def change_direction(cd):
    rd = 0

    if cd == 0:
        rd = 1
    elif cd == 1:
        rd = 0
    elif cd == 2:
        rd = 3
    else:
        rd = 2

    return rd

def move_to_white(unit_id, cr, cc, nr, nc):
    global mat_unit, unit_info
    
    cur_idx = mat_unit[cr][cc].index(unit_id)

    left_list = mat_unit[cr][cc][:cur_idx]
    moved_list = mat_unit[cr][cc][cur_idx:]

    mat_unit[cr][cc] = left_list
    mat_unit[nr][nc].extend(moved_list)
    
    for moved_unit_id in moved_list:
        ur, uc, ud = unit_info[moved_unit_id]
        unit_info[moved_unit_id] = [nr, nc, ud]

def move_to_red(unit_id, cr, cc, nr, nc):
    global mat_unit, unit_info
    
    cur_idx = mat_unit[cr][cc].index(unit_id)

    left_list = mat_unit[cr][cc][:cur_idx]
    moved_list = mat_unit[cr][cc][cur_idx:]
    moved_list.reverse()

    mat_unit[cr][cc] = left_list
    mat_unit[nr][nc].extend(moved_list)
    
    for moved_unit_id in moved_list:
        ur, uc, ud = unit_info[moved_unit_id]
        unit_info[moved_unit_id] = [nr, nc, ud]

def move_to_blue(unit_id, cr, cc, cd):
    global N, board, unit_info, dx, dy

    rd = change_direction(cd)

    rr, rc = cr + dy[rd], cc + dx[rd]
    unit_info[unit_id][2] = rd
    moved_r, moved_c = rr, rc
    
    if not (0 <= rr < N and 0 <= rc < N):
        moved_r, moved_c = cr, cc
    
    elif board[rr][rc] == 0:
        # 흰색
        move_to_white(unit_id, cr, cc, rr, rc)

    elif board[rr][rc] == 1:
        # 빨간색
        move_to_red(unit_id, cr, cc, rr, rc)

    elif board[rr][rc] == 2:
        # 파란색
        moved_r, moved_c = cr, cc

    return moved_r, moved_c


def move(unit_id, cr, cc, cd):
    global N, board, mat_unit, unit_info, dx, dy

    is_more_than_four = False
    nr, nc = cr + dy[cd], cc + dx[cd]
    moved_r, moved_c = nr, nc

    if 0 <= nr < N and 0 <= nc < N:
        if board[nr][nc] == 0:
            # 흰색
            move_to_white(unit_id, cr, cc, nr, nc)

        elif board[nr][nc] == 1:
            # 빨간색
            move_to_red(unit_id, cr, cc, nr, nc)

        else:
            # 파란색
            moved_r, moved_c = move_to_blue(unit_id, cr, cc, cd)

    else:
        moved_r, moved_c = move_to_blue(unit_id, cr, cc, cd)
    
    if len(mat_unit[moved_r][moved_c]) >= 4:
        is_more_than_four = True
        
    return is_more_than_four
    

if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().strip().split())

    board = [ list(map(int, sys.stdin.readline().strip().split())) for _ in range(N) ]
    mat_unit = []

    for i in range(N):
        temp_row = []
        for j in range(N):
            temp_row.append([])

        mat_unit.append(temp_row)

    unit_info = { unit_id: (0, 0, 0) for unit_id in range(1, K+1) } # (r, c, d)

    for unit_id in range(1, K+1):
        r, c, d = map(int, sys.stdin.readline().strip().split())

        r, c, d = r-1, c-1, d-1

        mat_unit[r][c].append(unit_id)
        unit_info[unit_id] = [r, c, d]

    dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]

    answer = -1

    for cur_turn in range(1, 1001):
        is_end = False
        
        for unit_id in range(1, K+1):
            cr, cc, cd = unit_info[unit_id]

            res = move(unit_id, cr, cc, cd)

            if res:
                is_end = True
                break
        
        if is_end:
            answer = cur_turn
            break
        
    print(answer)
