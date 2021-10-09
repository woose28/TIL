'''
    제출 언어: Python3
    시간: 108ms
'''
import sys

def check_row(r):
    global N, mat, answer

    prev = mat[r][0]
    cnt_score = 1

    for i in range(1, N):
        if prev == mat[r][i]:
            cnt_score += 1
        else:
            answer = max(answer, cnt_score)
            prev = mat[r][i]
            cnt_score = 1
    
    answer = max(answer, cnt_score)


def check_col(c):
    global N, mat, answer

    prev = mat[0][c]
    cnt_score = 1

    for i in range(1, N):
        if prev == mat[i][c]:
            cnt_score += 1
        else:
            answer = max(answer, cnt_score)
            prev = mat[i][c]
            cnt_score = 1
    
    answer = max(answer, cnt_score)


if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())

    mat = [ list(sys.stdin.readline().strip()) for _ in range(N) ]

    answer = 1
    
    for i in range(N):
        check_row(i)
        check_col(i)

    dx, dy = [0, 1], [1, 0]

    for i in range(N):
        for j in range(N):
            cr, cc = i, j
            for k in range(2):
                nr, nc = cr+dy[k], cc+dx[k]
                
                if 0 <= nr < N and 0 <= nc < N and mat[cr][cc] != mat[nr][nc]:
                    temp = mat[cr][cc]
                    mat[cr][cc] = mat[nr][nc]
                    mat[nr][nc] = temp

                    if k % 2 == 0:
                        check_col(cc)
                        check_row(cr)
                        check_row(nr)
                    
                    else:
                        check_row(cr)
                        check_col(cc)
                        check_col(nc)

                    mat[nr][nc] = mat[cr][cc]
                    mat[cr][cc] = temp
                    

    print(answer)

