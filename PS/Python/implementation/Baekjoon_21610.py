'''
    제출 언어: PyPy3
    시간: 184ms
'''
import sys

def move(d, s):
    global N, dy, dx, cloud_mat, cloud_list

    for i in range(len(cloud_list)):
        cr, cc = cloud_list[i]

        nr, nc = (cr+dy[d-1]*s) % N, (cc+dx[d-1]*s) % N
        cloud_list[i] = (nr, nc)

    for cloud in cloud_list:
        cr, cc = cloud

        cloud_mat[cr][cc] = True

def increase_water():
    global mat, cloud_list

    for cloud in cloud_list:
        cr ,cc = cloud

        mat[cr][cc] += 1

def increase_extra_water():
    global N, mat, dy, dx, cloud_list

    for cloud in cloud_list:
        cr, cc = cloud
        extra_water = 0

        for i in range(1, 8, 2):
            nr, nc = cr+dy[i], cc+dx[i]

            if 0 <= nr < N and 0 <= nc < N and mat[nr][nc] > 0:
                extra_water += 1

        mat[cr][cc] += extra_water

def create_cloud():
    global N, mat, cloud_mat, cloud_list

    total = 0
    temp_cloud = []

    for i in range(N):
        for j in range(N):

            if cloud_mat[i][j]:
                cloud_mat[i][j] = False
            
            elif not cloud_mat[i][j] and mat[i][j] >= 2:
                mat[i][j] -= 2
                temp_cloud.append([i, j])
            
            total += mat[i][j]

    cloud_list = temp_cloud

    return total

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().strip().split())

    mat = [ list(map(int, sys.stdin.readline().strip().split())) for _ in range(N) ]
    command_list = [ list(map(int, sys.stdin.readline().strip().split())) for _ in range(M) ]

    dy, dx = [0, -1, -1, -1, 0, 1, 1, 1], [-1, -1, 0, 1, 1, 1, 0, -1]
    
    cloud_list = [(N-2, 0), (N-2, 1), (N-1, 0), (N-1, 1)]
    cloud_mat = [ [ False ] * N for _ in range(N) ]
    
    answer = 0
    
    for command in command_list:
        d, s = command
        
        move(d, s)

        increase_water()

        increase_extra_water()

        answer = create_cloud()

    print(answer)
