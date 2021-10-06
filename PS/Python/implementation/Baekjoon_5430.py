'''
    제출 언어: Python3
    시간: 352ms
'''
import sys
from collections import deque

def solution(command, arr):
    length = len(arr)
    is_reversed = False
    is_error = False
    res = ""

    for c in command:
        if c == "R":
            is_reversed = not is_reversed
            
        else:
            if length > 0:
                length -= 1
                
                if is_reversed:
                    arr.pop()
                else:
                    arr.popleft()

            else:
                is_error = True
                break
    
    if is_reversed:
        arr.reverse()

    if is_error:
        res = "error"
    else:
        res = "[" + ",".join(list(map(str, arr))) + "]"

    return res

if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())
    
    answer = []

    for _ in range(T):
        command = sys.stdin.readline().strip()
        n = int(sys.stdin.readline().strip())
        arr = sys.stdin.readline().strip()

        if n == 0:
            arr = deque([])
            
        elif n == 1:
            arr = deque([int(arr[1:-1])])

        else:
            arr = deque(list(map(int, arr[1:-1].split(","))))

        answer.append(solution(command, arr))


    for res in answer:
        print(res)
