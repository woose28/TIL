'''
    제출 언어: Python3
    시간: 128ms
'''
import sys
from collections import Counter

if __name__ == "__main__":
    word1 = sys.stdin.readline().strip()
    word2 = sys.stdin.readline().strip()

    c1 = Counter(word1)
    c2 = Counter(word2)

    answer = 0

    for k in c1.keys():
        if k in word2:
            if c1[k] > c2[k]:
                answer += c1[k] - c2[k]

        else:
            answer += c1[k]

    for k in c2.keys():
        if k in word1:
            if c2[k] > c1[k]:
                answer += c2[k] - c1[k]
        
        else:
            answer += c2[k]

    print(answer)
        

