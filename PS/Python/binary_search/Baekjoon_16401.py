'''
    제출 언어: Python3
    시간: 1984ms
'''
import sys

if __name__ == "__main__":
    M, N = list(map(int, sys.stdin.readline().strip().split()))

    snack_list = list(map(int, sys.stdin.readline().strip().split()))

    answer = 0
    left = 1
    right = max(snack_list)

    while left <= right:
        mid = (left + right) // 2
        cnt = sum([ snack // mid for snack in snack_list ])

        if cnt >= M:
            answer = mid
            left = mid + 1

        else:
            right = mid - 1
    
    print(answer)

