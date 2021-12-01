'''
    제출 언어: Python3
    시간: 80ms
'''
import sys

if __name__ == "__main__":
    S = int(sys.stdin.readline().strip())

    cur_num = 0
    cur_sum = 0

    while cur_sum <= S:
        cur_num += 1
        cur_sum += cur_num

    answer = cur_num - 1

    print(answer)
    
