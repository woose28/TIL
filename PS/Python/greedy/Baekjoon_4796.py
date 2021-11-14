'''
    제출 언어: Python3
    시간: 68ms
'''
import sys

if __name__ == "__main__":
    
    answers = []

    while True:
        L, P, V = map(int, sys.stdin.readline().strip().split())
    
        if L == 0 and P == 0 and V == 0:
            break
        
        res = L * (V // P) + min(L, V % P)
        answers.append(res)

    for i in range(len(answers)):
        print(f"Case {i+1}: {answers[i]}")
    
