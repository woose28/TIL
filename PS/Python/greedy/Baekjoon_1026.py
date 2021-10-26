'''
    제출 언어: Python3
    시간: 84ms
'''
import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())

    A = list(map(int, sys.stdin.readline().strip().split()))
    B = list(map(int, sys.stdin.readline().strip().split()))

    A.sort(reverse=True)
    B.sort()

    answer = 0

    for i in range(N):
        answer += A[i] * B[i]

    print(answer)
