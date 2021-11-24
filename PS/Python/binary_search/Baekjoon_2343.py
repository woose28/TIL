'''
    제출 언어: Python3
    시간: 336ms
'''
import sys

def check(cur_size):
    global N, M, classes
    cnt_blueray = 1
    cur_time = 0

    for time in classes:
        if cur_time + time > cur_size:
            cnt_blueray += 1
            cur_time = time
        else:
            cur_time += time
    
    is_success = False

    if cnt_blueray <= M:
        is_success = True

    return is_success


def search():
    global N, M, classes

    left, right = max(classes), sum(classes)
    res = left

    while left <= right:
        mid = (left + right) // 2

        if check(mid):
            res = mid
            right = mid - 1

        else:
            left = mid + 1
        
    return res

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().strip().split())

    classes = list(map(int, sys.stdin.readline().strip().split()))

    res = search()

    print(res)
