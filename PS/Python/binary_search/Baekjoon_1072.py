'''
    제출 언어: Python3
    시간: 68ms
'''
import sys

def calculate(alpha):
    global X, Y
    
    new_rate = ((Y+alpha)*100) // (X+alpha)

    return new_rate

def solution():
    global X, Y, Z
    res = 0
    left, right = 1, X

    while left <= right:
        mid = (left + right) // 2

        new_rate = calculate(mid)

        if new_rate > Z:
            right = mid-1
        
        else:
            left = mid+1

    return right+1

if __name__ == "__main__":
    X, Y = map(int, sys.stdin.readline().strip().split())
    Z = ((Y * 100) // X)
    
    answer = -1

    if Z < 99:
        answer = solution()

    print(answer)