'''
    제출 언어: Python3
    시간: 72ms
'''
import sys
import math

def convert_num_to_str(num):
    num_to_str = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
    }

    converted = ""

    if num < 10:
        converted = num_to_str[num]

    else:
        share = num // 10
        remainder = num % 10

        converted = num_to_str[share] + " " + num_to_str[remainder]

    return converted

if __name__ == "__main__":
    M, N = map(int, sys.stdin.readline().strip().split())

    num_list = list(range(M, N+1))
    hash_str_to_num = {}

    for num in num_list:
        converted = convert_num_to_str(num)

        hash_str_to_num[converted] = num

    answer = [ str(value) for _, value in sorted(hash_str_to_num.items(), key=lambda x: x[0])]

    for i in range(0, math.ceil(len(answer)), 10):
        print(" ".join(answer[i: i+10]))
