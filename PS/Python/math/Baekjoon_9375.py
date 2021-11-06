'''
    제출 언어: Python3
    시간: 64ms
'''
import sys

def solution(clothes):
    res = 1
    info = {}

    for i in clothes:
        name, cloth_type = i

        if cloth_type in info:
            info[cloth_type] += 1

        else:
            info[cloth_type] = 1

    for i in info.values():
        res *= i + 1
    
    return res - 1


if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())

    for _ in range(T):
        n = int(sys.stdin.readline().strip())
        clothes = [ sys.stdin.readline().strip().split() for _ in range(n) ]

        res = solution(clothes)
        print(res)