'''
    제출 언어: Python3
    시간: 80ms
'''
import sys

def search(cur_idx):
    global N, M, num_list, stack

    if len(stack) == M:
        print(" ".join(list(map(str, stack))))
        return
    
    for i in range(cur_idx, N):
        stack.append(num_list[i])
        search(i)
        stack.pop()


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().strip().split())

    num_list = list(map(int, sys.stdin.readline().strip().split()))
    num_list.sort()

    stack = []

    search(0)

