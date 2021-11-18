'''
    제출 언어: Python3
    시간: 504ms
'''
import sys
from copy import copy, deepcopy

def copyMat():
    global mat_fish, mat_copied
    mat_copied = deepcopy(mat_fish)

def checkMovable(nr, nc):
    global mat_smell, scx, scy

    isMovable = False

    if 0 <= nr < 4 and 0 <= nc < 4 and (nr != scy or nc != scx) and mat_smell[nr][nc] == 0:
        isMovable = True

    return isMovable

def moveFish():
    global mat_fish, fdx, fdy

    new_mat = [ [ [] for _ in range(4) ]for _ in range(4) ]

    for i in range(4):
        for j in range(4):
            for d in mat_fish[i][j]:
                nr, nc = i + fdy[d], j + fdx[d]

                if checkMovable(nr, nc):
                    new_mat[nr][nc].append(d)

                else:
                    isMoved = False

                    for k in range(1, 8):
                        nr, nc = i + fdy[(d - k) % 8], j + fdx[(d - k) % 8]

                        if checkMovable(nr, nc):
                            isMoved = True
                            new_mat[nr][nc].append((d - k) % 8)
                            break
                    
                    if not isMoved:
                        new_mat[i][j].append(d)

    mat_fish = new_mat

def moveShark():
    global mat_fish, mat_smell, scx, scy, moving_list, sdx, sdy, cnt_fish

    max_removed, di = 0, 0
    is_first = True

    for i in range(64):
        pr, pc = scy, scx
        cur_removed = 0
        isMovable = True
        visited = []

        for d in moving_list[i]:
            nr, nc = pr+sdy[d], pc+sdx[d]

            if not (0 <= nr < 4 and 0 <= nc < 4):
                isMovable = False
                break
            
            if (nr, nc) not in visited:
                cur_removed += len(mat_fish[nr][nc])
                visited.append((nr, nc))
            pr, pc = nr, nc

        if isMovable:
            if max_removed == 0 and cur_removed == 0 and is_first:
                di = i
                is_first = False

            elif max_removed < cur_removed:
                max_removed = cur_removed
                di = i

    pr, pc = scy, scx

    for d in moving_list[di]:
        nr, nc = pr+sdy[d], pc+sdx[d]
        
        if len(mat_fish[nr][nc]) > 0:
            cnt_fish -= len(mat_fish[nr][nc])
            mat_fish[nr][nc] = []
            mat_smell[nr][nc] = 3
        
        pr, pc = nr, nc

    scy, scx = nr, nc

def removeAndPaste():
    global mat_fish, mat_copied, mat_smell, cnt_fish

    for i in range(4):
        for j in range(4):
            if mat_smell[i][j] != 0:
                mat_smell[i][j] -= 1

            if len(mat_copied[i][j]) != 0:
                cnt_fish += len(mat_copied[i][j])
                mat_fish[i][j].extend(mat_copied[i][j])
    

def getSharkMovingList(cur_length):
    global moving_list, temp_list

    if cur_length == 3:
        moving_list.append(copy(temp_list))
        return

    for i in range(4):
        temp_list.append(i)
        getSharkMovingList(cur_length+1)
        temp_list.pop()


if __name__ == "__main__":
    M, S = map(int, sys.stdin.readline().strip().split())

    mat_fish = [ [ [] for _ in range(4) ]for _ in range(4) ]
    mat_smell = [ [0] * 4 for _ in range(4) ]
    mat_copied = []

    fdx, fdy = [-1, -1, 0, 1, 1, 1, 0, -1], [0, -1, -1, -1, 0, 1, 1, 1]
    sdx, sdy = [0, -1, 0, 1], [-1, 0, 1, 0]
    
    cnt_fish = M

    for _ in range(M):
        fx, fy, d = map(int, sys.stdin.readline().strip().split())

        fx, fy, d = fx - 1, fy - 1, d - 1
        mat_fish[fx][fy].append(d)

    scy, scx = map(int, sys.stdin.readline().strip().split())
    scy, scx = scy - 1, scx - 1

    moving_list = []
    temp_list = []
    getSharkMovingList(0)

    for _ in range(S):
        copyMat()
        moveFish()
        moveShark()
        removeAndPaste()

    answer = 0
    for i in range(4):
        for j in range(4):
            answer += len(mat_fish[i][j])

    print(answer)
