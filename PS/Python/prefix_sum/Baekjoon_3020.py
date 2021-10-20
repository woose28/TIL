'''
    제출 언어: Python3
    시간: 604ms
'''
import sys

def solution():
    global N, H, obstacles, o1, o2, dp

    for i in range(N):
        oh = obstacles[i]

        if i % 2 == 0:
            o1[H-oh] += 1

        else:
            o2[oh-1] += 1

    for i in range(1, H):
        o1[i] += o1[i-1]
        o2[H-i-1] += o2[H-i]

    for i in range(H):
        dp[i] = o1[i] + o2[i]
    

if __name__ == "__main__":
    N, H = map(int, sys.stdin.readline().strip().split())

    obstacles = [ int(sys.stdin.readline().strip()) for _ in range(N) ]
    dp = [ 0 ] * H
    o1 = [ 0 ] * H
    o2 = [ 0 ] * H

    solution()
    
    dp.sort()

    min_num = dp[0]
    cnt = 0

    for i in dp:
        if i == min_num:
            cnt += 1
        else:
            break
    
    print(min_num, cnt)
