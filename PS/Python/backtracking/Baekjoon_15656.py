'''
    제출 언어: Python3
    시간: 1944ms
'''
import sys

def search(length):
    global N, M, num_list, selected

    if length == M:
        print(" ".join(list(map(str, selected))))
        return

    for i in range(N):
        selected.append(num_list[i])
        search(length+1)
        selected.pop()


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().strip().split())

    num_list = list(map(int, sys.stdin.readline().strip().split()))
    num_list.sort()

    selected = []

    search(0)

