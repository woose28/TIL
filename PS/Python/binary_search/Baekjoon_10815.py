'''
    제출 언어: Python3
    시간: 2868ms
'''
import sys

def search(target):
    global N, num_list
    
    res = 0
    left, right = 0, N-1

    while left <= right:
        mid = (left+right) // 2

        if num_list[mid] == target:
            res = 1
            break
        elif num_list[mid] < target:
            left = mid+1
        else:
            right = mid-1

    return res

if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    num_list = sorted(map(int, sys.stdin.readline().strip().split()))

    M = int(sys.stdin.readline().strip())
    find_num_list = list(map(int, sys.stdin.readline().strip().split()))

    for i in range(M):
        res = search(find_num_list[i])

        if i == M-1:
            print(res)
        else:
            print(res, end=" ")
    
