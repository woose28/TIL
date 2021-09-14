'''
    제출 언어: PyPy3
    시간: 1400ms
    브루트포스, 구현, dfs 문제가 약한 거 같다.
    주로 시간 초과 문제가 발생하는 데 아래의 방법 들을 도입하는 게 익숙해져야 할 거 같다.
    1. 탐색 범위를 최소화 시키는 방법
    2. deepcopy를 이용한 배열 복사가 아닌 하나의 배열에서 방문 여부를 확인 하는 방법
'''
import sys

def check_is_success():
    global N, H, mat

    is_success = True

    for i in range(1, N+1):
        d = 0
        idx_left, idx_right = i-1, i

        for j in range(H):
            if mat[j][idx_left]:
                d -= 1
                idx_left -= 1
                idx_right -= 1   
                
            elif mat[j][idx_right]:
                d += 1
                idx_left += 1
                idx_right += 1
        
        if d != 0:
            is_success = False
            break
    
    return is_success

def solution(cur_cnt, x, y):
    global answer, N, H

    if check_is_success():
        if answer == -1 or answer > cur_cnt:
            answer = cur_cnt
        
        return

    if cur_cnt >= 3 or (answer != -1 and answer <= cur_cnt):
        return
    
    for i in range(y, H):
        sc = x if i == y else 1

        for j in range(sc, N):
            if mat[i][j]:
                continue
            
            elif mat[i][j-1] or mat[i][j+1]:
                continue

            mat[i][j] = True
            solution(cur_cnt+1, j+1, i)
            mat[i][j] = False
            
if __name__ == "__main__":
    N, M, H = map(int, sys.stdin.readline().strip().split())

    mat = [ [ False ] * (N+1) for _ in range(H) ]

    for _ in range(M):
        a, b = map(int, sys.stdin.readline().strip().split())
        mat[a-1][b] = True

    answer = -1

    solution(0, 1, 0)

    print(answer)

