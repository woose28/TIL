'''
    제출 언어: Python3
    시간: 396ms
'''
import sys

def check(d):
    global N, pos

    cc = 1
    cp = pos[0]

    for i in range(1, N):
        if pos[i] - cp >= d:
            cc += 1
            cp = pos[i]

    return cc

def solution():
    global N, C, pos

    left, right = 1, pos[-1] - pos[0]
    res = 0

    while left <= right:
        mid = (left+right) // 2

        if check(mid) >= C:
            res = mid        
            left = mid + 1
        
        else:
            right = mid -1

    return res


if __name__ == "__main__":
    N, C = map(int, sys.stdin.readline().strip().split())

    pos = [ int(sys.stdin.readline().strip()) for _ in range(N) ]
    pos.sort()

    answer = solution()
    print(answer)

