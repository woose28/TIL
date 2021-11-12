'''
    제출 언어: Python3
    시간: 68ms
'''
import sys

def solution():
    global doc, target

    res = 0
    ci = 0
    dl, tl = len(doc), len(target)

    if dl >= tl:
        while ci <= dl-1:
            if ci+tl > dl:
                break 
            
            if doc[ci: ci+tl] == target:
                res += 1
                ci = ci+tl
            
            else:
                ci += 1
    
    return res

if __name__ == "__main__":
    doc = sys.stdin.readline().strip()
    target = sys.stdin.readline().strip()

    answer = solution()

    print(answer)

