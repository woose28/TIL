'''
    제출 언어: Python3
    시간: 80ms
'''
import sys

def solution(ps):
    is_vps = "YES"
    validator = 0

    for c in ps:
        if validator < 0:
            break
        
        if c == "(":
            validator += 1

        else:
            validator -= 1
        
    if validator != 0:
        is_vps = "NO"
    
    return is_vps

if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())

    answer = []

    for _ in range(T):
        ps = sys.stdin.readline().strip()

        res = solution(ps)
        answer.append(res)
    
    for res in answer:
        print(res)
    