'''
    제출 언어: Python3
    시간: 140ms
'''
import sys

def recursive(cur_sum, prev_num, cur_cnt):
    global N, num_list, visited, answer

    if cur_cnt == N:
        answer = max(answer, cur_sum)
        return

    for i in range(N):
        if not visited[i]:
            next_sum = cur_sum + abs(prev_num - num_list[i])

            visited[i] = True
            recursive(next_sum, num_list[i], cur_cnt+1)
            visited[i] = False


if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    num_list = list(map(int, sys.stdin.readline().strip().split()))
    visited = [ False ] * N

    answer = 0
    
    for i in range(N):
        visited[i] = True
        recursive(0, num_list[i], 1)
        visited[i] = False
        
    print(answer)