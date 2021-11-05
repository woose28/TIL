'''
    제출 언어: Python3
    시간: 132ms
'''
import sys

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().strip().split())

    n_list = set([ sys.stdin.readline().strip() for _ in range(N) ])
    m_list = set([ sys.stdin.readline().strip() for _ in range(M) ])

    t_list = list(n_list & m_list)
    
    print(len(t_list))
    t_list.sort()

    for e in t_list:
        print(e)

