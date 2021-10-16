'''
    제출 언어: PyPy3
    시간: 304ms
'''
import sys

def use_skill(nr, nc, cur_idx):
    global N, mat, answer

    effect_range = [
        [ (-1, -1), (1, -1), (-1, 0), (1, 0), (0, -2), (-2, 0), (2, 0), (-1, 1), (1, 1), (0, -1) ],
        [ (1, -1), (1, 1), (0, -1), (0, 1), (2, 0), (0, -2), (0, 2), (-1, -1), (-1, 1), (1, 0) ],
        [ (-1, 1), (1, 1), (-1, 0), (1, 0), (0, 2), (-2, 0), (2, 0), (-1, -1), (1, -1), (0, 1) ],
        [ (-1, -1), (-1, 1), (0, -1), (0, 1), (-2, 0), (0, -2), (0, 2), (1, -1), (1, 1), (-1, 0) ]
    ]
    rate = [ 10, 10, 7, 7, 5, 2, 2, 1, 1 ]

    tot_sand = mat[nr][nc]
    using = 0

    for i in range(9):
        er, ec = nr + effect_range[cur_idx][i][0], nc + effect_range[cur_idx][i][1]
        e_rate = rate[i]

        e_sand = (tot_sand * e_rate) // 100

        using += e_sand

        if 0 <= er < N and 0 <= ec < N:
            mat[er][ec] += e_sand
        
        else:
            answer += e_sand

    er, ec = nr + effect_range[cur_idx][9][0], nc + effect_range[cur_idx][9][1]

    if 0 <= er < N and 0 <= ec < N:
        mat[er][ec] +=  tot_sand - using

    else:
        answer += tot_sand - using

    mat[nr][nc] = 0


if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())

    mat = [ list(map(int, sys.stdin.readline().strip().split())) for _ in range(N) ]

    cur_pos = (N//2, N//2)

    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    cur_idx = 0
    cd = 0

    answer = 0

    while True:
        cr, cc=  cur_pos

        if cr == 0 and cc == 0:
            break

        if cur_idx % 2 == 0:
            cd += 1

        for _ in range(cd):
            nr, nc = cr+dy[cur_idx], cc+dx[cur_idx]

            use_skill(nr, nc, cur_idx)

            cr, cc = nr, nc

            if cr == 0 and cc == 0:
                break
            
        cur_idx = (cur_idx+1) % 4
        cur_pos = (cr, cc)

    print(answer)