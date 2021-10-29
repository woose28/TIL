'''
    제출 언어: Python3
    시간: 92ms
'''
import sys

if __name__ == "__main__":
    S = sys.stdin.readline().strip()

    answer = ""
    candidate_tag = ""
    candidate_string = ""
    is_open = False

    for c in S:
        if is_open:
            if c == ">":
                answer += candidate_tag + c
                candidate_tag = ""
                is_open = False
            else:
                candidate_tag += c

        else:
            if c == "<":
                answer += candidate_string[::-1]
                candidate_string = ""
                candidate_tag = "<"
                is_open = True
            
            elif c == " ":
                answer += candidate_string[::-1] + c
                candidate_string = ""
            
            else:
                candidate_string += c

    if len(candidate_string) != 0:
        answer += candidate_string[::-1]

    print(answer)
