'''
    제출 언어: Python3
    시간: 72ms
'''
import sys

def recursive(cur_idx, selected):
    global K, num_list

    if len(selected) == 6:
        print(" ".join(selected))
        return

    for i in range(cur_idx+1, K):
        next = selected + [num_list[i]]
        recursive(i, next)
    
if __name__ == "__main__":
    while True:
        input_data = sys.stdin.readline().strip().split()

        if input_data[0] == "0":
            break

        K, num_list = int(input_data[0]), input_data[1:]

        recursive(-1, [])
        print()

