'''
    제출 언어: Python3
    시간: 68ms
'''
import sys

def gcd(n, m):

    while m != 0:
        n, m = m, n % m
    
    return n


def lcm(n, m):
    return (n * m) // gcd(n, m)

if __name__ == "__main__":
    a1, b1 = map(int, sys.stdin.readline().strip().split())
    a2, b2 = map(int, sys.stdin.readline().strip().split())

    d1 = lcm(b1, b2)
    n1 = a1 * (d1 // b1) + a2 * (d1 // b2)

    cd1 = gcd(d1, n1)

    print(n1 // cd1, d1 // cd1)

