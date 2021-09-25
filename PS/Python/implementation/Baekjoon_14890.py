'''
    제출 언어: PyPy3
    시간: 112ms
'''
import sys

def check_row():
    global N, L, mat, answer

    is_slope = [ [False] * N for _ in range(N) ]

    for r in range(N):
        cc = 1
        is_success = True

        while cc < N:
            if mat[r][cc-1] == mat[r][cc]:
                cc += 1
            
            elif mat[r][cc-1] == mat[r][cc]+1:
                cnt_free = 0

                for nc in range(cc, cc+L):
                    if nc >= N or mat[r][cc] != mat[r][nc] or is_slope[r][nc]:
                        break
                    
                    cnt_free += 1

                if cnt_free == L:
                    for nc in range(cc, cc+L):
                        is_slope[r][nc] = True
                    cc += L
                else:
                    is_success = False
                    break
                
            elif mat[r][cc-1] == mat[r][cc]-1:
                cnt_free = 0

                for nc in range(cc-1, cc-1-L, -1):
                    if nc < 0 or mat[r][cc] != mat[r][nc]+1 or is_slope[r][nc]:
                        break

                    cnt_free += 1
                
                if cnt_free == L:
                    for nc in range(cc-1, cc-1-L, -1):
                        is_slope[r][nc] = True
                    cc += 1
                else:
                    is_success = False
                    break

            else:
                is_success = False
                break
        
        if is_success:
            answer += 1

def check_col():
    global N, L, mat, answer

    is_slope = [ [False] * N for _ in range(N) ]

    for c in range(N):
        cr = 1
        is_success = True

        while cr < N:
            if mat[cr-1][c] == mat[cr][c]:
                cr += 1
            
            elif mat[cr-1][c] == mat[cr][c]+1:
                cnt_free = 0

                for nr in range(cr, cr+L):
                    if nr >= N or mat[cr][c] != mat[nr][c] or is_slope[nr][c]:
                        break
                    
                    cnt_free += 1

                if cnt_free == L:
                    for nr in range(cr, cr+L):
                        is_slope[nr][c] = True
                    cr += L
                else:
                    is_success = False
                    break
                
            elif mat[cr-1][c] == mat[cr][c]-1:
                cnt_free = 0

                for nr in range(cr-1, cr-1-L, -1):
                    if nr < 0 or mat[cr][c] != mat[nr][c]+1 or is_slope[nr][c]:
                        break

                    cnt_free += 1
                
                if cnt_free == L:
                    for nr in range(cr-1, cr-1-L, -1):
                        is_slope[nr][c] = True
                    cr += 1
                else:
                    is_success = False
                    break

            else:
                is_success = False
                break
        
        if is_success:
            answer += 1

if __name__ == "__main__":
    N, L = map(int, sys.stdin.readline().strip().split())

    mat = [ list(map(int, sys.stdin.readline().strip().split())) for _ in range(N) ]
    
    answer = 0

    check_row()
    check_col()
    
    print(answer)


