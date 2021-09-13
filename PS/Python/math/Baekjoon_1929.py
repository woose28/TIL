'''
    제출 언어: PyPy3
    시간: 192ms
    에라토스테네스의 체
'''
import sys

def solution(N):
    global num_list

    end_num = int((N ** 0.5))

    for i in range(2, end_num+1):
        if num_list[i]:
           for j in range(i*2, N+1, i):
               num_list[j] = False


if __name__ == "__main__":
    M, N = map(int, sys.stdin.readline().strip().split())

    num_list = [ True ] * (N + 1)
    num_list[1] = False
    
    solution(N)

    for idx in range(M, N+1):
        if num_list[idx]:
            print(idx)
            
