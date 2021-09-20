'''
    제출 언어: Python3
    시간: 440ms
'''
import sys

def solution():
    global n, cities

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if cities[i][j] > cities[i][k] + cities[k][j]:
                    cities[i][j] = cities[i][k] + cities[k][j]

    for i in range(n):
        for j in range(n):
            if cities[i][j] == float('inf'):
                cities[i][j] = 0

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    m = int(sys.stdin.readline().strip())

    cities = [ [ float('inf') ] * n for _ in range(n) ]

    for i in range(n):
        cities[i][i] = 0
    
    for _ in range(m):
        s, e, f = map(int, sys.stdin.readline().strip().split())
        
        if cities[s-1][e-1] > f:
            cities[s-1][e-1] = f
    
    solution()

    for i in range(n):
        print(" ".join(map(str, cities[i])))
