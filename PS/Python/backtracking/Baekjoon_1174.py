'''
    제출 언어: Python3
    시간: 72ms
'''
import sys

def recursion(prev_num, cur_num, cur_length):
    global N, target_length, cnt_decreasing_num, answer

    if cur_length == target_length:
        cnt_decreasing_num += 1

        if cnt_decreasing_num == N:
            answer = prev_num + str(cur_num)

        return
    
    for i in range(0, cur_num):
        recursion(prev_num + str(cur_num), i, cur_length + 1)


if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())

    target_length = 1
    cnt_decreasing_num = 0
    answer = -1

    while target_length <= 10:
        for i in range(target_length-1, 10):
            recursion('', i, 1)

        if answer != -1:
            break
        
        target_length += 1

    print(answer)