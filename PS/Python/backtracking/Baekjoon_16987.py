'''
    제출 언어: Python3
    시간: 4964ms
'''
import sys

def is_all_broken(cur_idx):
    global N, eggs

    result = True

    for i in range(N):
        d, w = eggs[i]

        if i != cur_idx and d > 0:
            result = False
            break

    return result

def recursion(cur_idx, cur_broken):
    global N, eggs, answer

    if cur_idx == N:
        if answer < cur_broken:
            answer = cur_broken
        return

    cd, cw = eggs[cur_idx]

    if cd <= 0 or is_all_broken(cur_idx):
        recursion(cur_idx+1, cur_broken)
    
    else:
        for i in range(N):
            nd, nw = eggs[i]

            if i == cur_idx or nd <= 0:
                continue

            after_cd = cd - nw
            after_nd = nd - cw
            after_broken = 0

            if after_cd <= 0:
                after_broken += 1
            
            if after_nd <= 0:
                after_broken += 1
            
            eggs[cur_idx] = [after_cd, cw]
            eggs[i] = [after_nd, nw]

            recursion(cur_idx+1, cur_broken + after_broken)

            eggs[cur_idx] = [cd, cw]
            eggs[i] = [nd, nw]
            

if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())

    eggs = [ list(map(int, sys.stdin.readline().strip().split())) for _ in range(N) ]

    answer = 0

    recursion(0, 0)
    
    print(answer)