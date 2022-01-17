'''
    제출 언어: Python3
    시간: 88ms
'''
import sys

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().strip().split())

    mat = [ list(sys.stdin.readline().strip()) for _ in range(N) ]

    answer = 1

    for i in range(N-1):
        for j in range(M-1):
            ul = mat[i][j]

            for k in range(j+1, M):
                if mat[i][k] == ul:
                    if i + (k-j) < N and mat[i + (k-j)][j] == ul and mat[i + (k-j)][k] == ul and answer < (k-j+1) ** 2:
                        answer = (k-j+1) ** 2
                    
                
            
        
    
    print(answer)

