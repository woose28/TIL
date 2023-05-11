import sys

K, N = map(int, sys.stdin.readline().split(' '))

L = []
moving_time = {}

for i in range(N):
    data = list(map(int, sys.stdin.readline().split(' ')))

    moving_time[i] = {}
    L.append(data[:K])
    
    if i == N-1:
        continue
    
    for j in range(K):
        cur_moving_time = data[K + (K-1) * j: K + (K-1) * (j + 1)]
        cur_moving_time.insert(j, 0)

        moving_time[i][j] = cur_moving_time


def solution(K, N, L, moving_time):
    acc_time = L[0]

    for cur_work in range(N - 1):
        next_moving_times = []

        for next_line in range(K):
            next_line_min_time = float('inf')

            for cur_line in range(K):
                next_line_time = acc_time[cur_line] + moving_time[cur_work][cur_line][next_line] + L[cur_work + 1][next_line]

                if next_line_min_time > next_line_time:
                    next_line_min_time = next_line_time
            
            next_moving_times.append(next_line_min_time)
    
        acc_time = next_moving_times

    print(min(acc_time))\

solution(K, N, L, moving_time)