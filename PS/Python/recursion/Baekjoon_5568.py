'''
    제출 언어: Python3
    시간: 72ms
'''
import sys

def select_card(cnt_selected, cur_num):
    global n, k, card_list, used

    if cnt_selected == k:
        num_list.add(cur_num)
        return
    
    for i in range(n):
        if not used[i]:
            used[i] = True
            select_card(cnt_selected + 1, cur_num + card_list[i])
            used[i] = False
    

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    k = int(sys.stdin.readline().strip())

    card_list = [ sys.stdin.readline().strip() for _ in range(n) ]
    used = [ False ] * n

    num_list = set()

    select_card(0, "")

    print(len(num_list))
