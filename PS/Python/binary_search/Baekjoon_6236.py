'''
    제추 언어: Python3
    시간: 320ms
'''
import sys

def check(K):
    global spend_list

    remaining_money = 0
    cnt = 0

    for cur_money in spend_list:
        if remaining_money >= cur_money:
            remaining_money -= cur_money

        else:
            cnt += 1
            remaining_money = (K - cur_money)

    return cnt

def search():
    global M, spend_list

    left, right = max(spend_list), sum(spend_list)

    while left <= right:
        mid = (left + right) // 2

        cur_cnt = check(mid)

        if cur_cnt <= M:
            right = mid - 1

        else:
            left = mid + 1

    res = left

    return res

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().strip().split())

    spend_list = []

    for _ in range(N):
        spend_list.append(int(sys.stdin.readline().strip()))
    
    answer = search()

    print(answer)
