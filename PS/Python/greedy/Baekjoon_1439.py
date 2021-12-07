'''
    제출 언어: Python3
    시간: 72ms
'''
import sys

if __name__ == "__main__":
    S = sys.stdin.readline().strip()

    cnt_part_0 = 0
    cnt_part_1 = 0

    prev_num = S[0]

    for i in range(1, len(S)):
        cur_num = S[i]
        
        if cur_num != prev_num:
            if prev_num == '0':
                cnt_part_0 += 1
                pass

            else:
                cnt_part_1 += 1
                pass

            prev_num = cur_num

    if prev_num == '0':
        cnt_part_0 += 1
    else:
        cnt_part_1 += 1

    answer = min(cnt_part_0, cnt_part_1)

    print(answer)
