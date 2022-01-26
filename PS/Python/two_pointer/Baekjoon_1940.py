'''
    제출 언어: Python3
    시간: 76ms
'''
import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    M = int(sys.stdin.readline().strip())
    num_list = list(map(int, sys.stdin.readline().strip().split()))

    num_list.sort()

    left, right = 0, N - 1
    answer = 0

    while left < right:
        if num_list[left] + num_list[right] == M:
            left += 1
            right -= 1
            answer += 1

        elif num_list[left] + num_list[right] < M:
            left += 1
        
        else:
            right -= 1

    print(answer)
        

