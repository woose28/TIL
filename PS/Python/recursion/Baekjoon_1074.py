'''
    제출 언어: Python3
    시간: 68ms
'''
import sys

def search(sr, sc, n):
    global cur_num
    if n == 0:
        cur_num += 1

        if sr == r and sc == c:
            print(cur_num)
        
        return
    
    if sr <= r < sr+2**(n-1) and sc <= c < sc+2**(n-1):
        search(sr, sc, n-1)

    elif sr <= r < sr+2**(n-1) and sc+2**(n-1) <= c < sc+2**(n):
        cur_num += 2**(n-1) * 2**(n-1)
        search(sr, sc+2**(n-1), n-1)

    elif sr+2**(n-1) <= r < sr+2**(n) and sc <= c < sc+2**(n-1):
        cur_num += (2**(n-1) * 2**(n-1))*2
        search(sr+2**(n-1), sc, n-1)
    
    else:
        cur_num += (2**(n-1) * 2**(n-1))*3
        search(sr+2**(n-1), sc+2**(n-1), n-1)
    

if __name__ == "__main__":
    N, r, c = map(int, sys.stdin.readline().strip().split())

    cur_num = -1

    search(0, 0, N)
