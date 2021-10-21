'''
    제출 언어: Python3
    시간: 76ms
'''
import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())

    num_list = list(map(int, sys.stdin.readline().strip().split()))

    num_list.sort()

    answer = num_list[0] * num_list[-1]

    print(answer)