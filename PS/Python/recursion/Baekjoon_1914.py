'''
    제출 언어: Python3
    시간: 1096ms
'''
import sys

def hanoi(n, start, end):
    if n < 1:
        return

    hanoi(n-1, start, 6 - (start+end))
    print(start, end)
    hanoi(n-1, 6 - (start+end), end)

if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())

    print(2 ** N - 1)

    if N <= 20:
        hanoi(N, 1, 3)
