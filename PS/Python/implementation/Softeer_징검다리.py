import sys

N = int(sys.stdin.readline())
stones = list(map(int, sys.stdin.readline().split(' ')))

def solution(N, stones):
    answer = 0
    min_stone_height = float('inf')

    stepable_stone_count = [ 0 for _ in range(N) ]
    stepable_stone_count[N - 1] = 1

    for i in range(N - 2, -1, -1):
        cur_stone_height = stones[i]
        cur_stepable_stone_count = 1

        for j in range(i, N):
            next_stone_height = stones[j]

            if cur_stone_height < next_stone_height:
                if cur_stepable_stone_count < stepable_stone_count[j] + 1:
                    cur_stepable_stone_count = stepable_stone_count[j] + 1
        
        stepable_stone_count[i] = cur_stepable_stone_count

    answer = max(stepable_stone_count)
    
    print(answer)    

solution(N, stones)