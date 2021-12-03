'''
    제출 언어: Python3
    시간: 76ms
'''
import sys

def recursive(cur_idx, length):
    global N, M, num_list, selected

    if length == M:
        print(" ".join(map(str, selected)))
        return

    last_selected = 0

    for i in range(cur_idx+1, N):
        if last_selected != num_list[i]:
            selected.append(num_list[i])
            last_selected = num_list[i]
            recursive(i, length+1)
            selected.pop()
        
if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().strip().split())

    num_list = list(map(int, sys.stdin.readline().strip().split()))
    num_list.sort()

    selected = []

    recursive(-1, 0)
