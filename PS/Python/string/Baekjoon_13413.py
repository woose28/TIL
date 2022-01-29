'''
    제출 언어: Python3
    시간: 2048ms
'''
import sys

if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())

    for _ in range(T):
        N = int(sys.stdin.readline().strip())
        initial_state = list(sys.stdin.readline().strip())
        target_state = list(sys.stdin.readline().strip())

        initial_w_cnt = 0
        target_w_cnt = 0
        diff_piece_cnt = 0
        diff_pos_cnt = 0

        for i in range(N):
            if initial_state[i] == "W":
                initial_w_cnt += 1

            if target_state[i] == "W":
                target_w_cnt += 1

            if initial_state[i] != target_state[i]:
                diff_pos_cnt += 1

        diff_piece_cnt = abs(initial_w_cnt - target_w_cnt)

        print((diff_pos_cnt - diff_piece_cnt) // 2 + diff_piece_cnt)
    