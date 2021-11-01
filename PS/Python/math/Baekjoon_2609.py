'''
    제출 언어: Python3
    시간: 72ms
'''
import sys

def gcd(a, b):
    while b != 0:
        a, b = b, a % b

    return a

if __name__ == "__main__":
    a, b = map(int, sys.stdin.readline().strip().split())

    gcd_num = gcd(max(a, b), min(a, b))
    lcm_num = (a * b) // gcd_num

    print(gcd_num)
    print(lcm_num)

