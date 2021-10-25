'''
    제출 언어: Python3
    시간: 2972ms
'''
import sys

def cut(h):
    global N, M, tree_list

    length = 0

    for t in tree_list:
        if t > h:
            length += t - h

    return length

def solution():
    global N, M, tree_list

    tree_list.sort()

    left, right = 0, tree_list[-1]
    res = 0

    while left <= right:
        mid = (left+right) // 2

        cur_length = cut(mid)

        if cur_length >= M:
            res = mid
            left = mid+1
        
        else:
            right = mid-1
        
    return res

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().strip().split())

    tree_list = list(map(int, sys.stdin.readline().strip().split()))

    answer = solution()

    print(answer)
    