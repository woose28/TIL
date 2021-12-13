'''
    제출 언어: Python3
    시간: 140ms
'''
import sys
from collections import Counter

if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())

    for _ in range(N):
        w1, w2 = sys.stdin.readline().strip().split()

        if Counter(w1) == Counter(w2):
            print('Possible')

        else:
            print('Impossible')
    
