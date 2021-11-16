'''
    제출 언어: Python3
    시간: 68ms
'''
import sys

def search(cur_idx, length):
    global N, M, num_list, seq

    if length == M:
        print(" ".join(list(map(str, seq))))
        return

    for i in range(cur_idx+1, N):
        seq.append(num_list[i])
        search(i, length+1)
        seq.pop()

    pass
if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().strip().split())

    num_list = list(map(int, sys.stdin.readline().strip().split()))
    num_list.sort()
    seq = []

    search(-1, 0)


