'''
    제출 언어: Python3
    시간: 112ms
'''
import sys

if __name__ == "__main__":
    answers = []

    while True:
        inputed_data = sys.stdin.readline().rstrip()

        if inputed_data == ".":
            break

        bracket = []

        res = "yes"

        for c in inputed_data:
            if c == "(" or c == "[":
                bracket.append(c)

            elif c == ")" or c == "]":
                if len(bracket) == 0:
                    res = "no"
                    break

                item = bracket.pop()
                    
                if not ((c == ")" and item == "(") or (c == "]" and item == "[")):
                    res = "no"
                    break

        if len(bracket) != 0:
            res = "no"

        answers.append(res)

    for answer in answers:
        print(answer)
    
