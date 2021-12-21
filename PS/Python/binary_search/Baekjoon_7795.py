'''
    제출 언어: Python3
    시간: 336ms
'''
import sys

def search(target, left_idx):
    global B, N, M

    left = left_idx
    right = M  - 1

    while left <= right:
        mid = (left + right) // 2

        if target > B[mid]:
            left = mid + 1

        else:
            right = mid - 1

    return left

if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())

    for _ in range(T):
        N, M = map(int, sys.stdin.readline().strip().split())

        A = list(map(int, sys.stdin.readline().strip().split()))
        B = list(map(int, sys.stdin.readline().strip().split()))

        A.sort()
        B.sort()

        answer = 0
        left_idx = 0

        for i in range(N):
            left_idx = search(A[i], left_idx)
            answer += left_idx

        print(answer)

