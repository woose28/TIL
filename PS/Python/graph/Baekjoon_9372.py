'''
    제출 언어: Python3
    시간: 196ms
'''
import sys

if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())

    for _ in range(T):
        N, M = map(int, sys.stdin.readline().strip().split())

        for _ in range(M):
            a, b = map(int, sys.stdin.readline().strip().split())
        
        print(N-1)

