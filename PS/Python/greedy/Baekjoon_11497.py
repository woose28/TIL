'''
    제출 언어: Python3
    시간: 284ms
'''
import sys

if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())

    N_list = []
    num_lists = []
    for _ in range(T):
        N = int(sys.stdin.readline().strip())
        num_list = list(map(int, sys.stdin.readline().strip().split()))
        num_list.sort()

        N_list.append(N)
        num_lists.append(num_list)

    for i in range(T):
        N = N_list[i]
        num_list = num_lists[i]

        answer = max(num_list[N-1] - num_list[N-2], num_list[N-1] - num_list[N-3])

        for i in range(N-2, 1, -1):
            answer = max(answer, num_list[i] - num_list[i-2])

        answer = max(answer, num_list[1] - num_list[0])

        print(answer)
