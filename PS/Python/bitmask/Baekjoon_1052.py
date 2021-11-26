'''
    제출 언어: Pypy3
    시간: 748ms
'''
import sys

def check(target):
    global N

    cnt = 0
    curNum = N + target

    while curNum != 0:
        cnt += curNum % 2
        curNum = curNum // 2
        
    return cnt

def findNextPowersOfTwo():
    global N

    num = 4

    while num < N:
        num *= 2
    
    return num

def search():
    global N, K

    res = -1

    endNum = findNextPowersOfTwo() - N

    for i in range(0, endNum+1):
        if check(i) <= K:
            res = i
            break

    return res
    
def isPowersOfTwo(num):
    return (num & num-1) == 0

if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().strip().split())

    if isPowersOfTwo(N):
        print(0)

    else:
        answer = search()
        print(answer)
    