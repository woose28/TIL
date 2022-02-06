'''
    제출 언어: Python3
    시간: 528ms
'''
import sys

if __name__ == "__main__":
    K, L = list(map(int, sys.stdin.readline().strip().split()))

    waiting_list = {}

    for i in range(L):
        std_id = sys.stdin.readline().strip()

        waiting_list[std_id] = i

    sorted_list = sorted(waiting_list.items(), key = lambda x: x[1])

    for std_id, _ in sorted_list[:K]:
        print(std_id)

