'''
    제출 언어: Python3
    시간: 212ms
'''
import sys

def search(cur_list, cur_length):
    global N, M, num_list, visited

    if cur_length == M:
        print(" ".join(list(map(str, cur_list))))
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            search(cur_list+[ num_list[i] ], cur_length+1)
            visited[i] = False

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().strip().split())

    num_list = list(map(int, sys.stdin.readline().strip().split()))
    visited = [ False ] * N

    num_list.sort()

    search([], 0)

