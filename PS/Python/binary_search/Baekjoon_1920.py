import sys

def findNum(target):
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

    target_list = map(int, sys.stdin.readline().strip().split())
    
    for t in target_list:
        print(findNum(t))
    
