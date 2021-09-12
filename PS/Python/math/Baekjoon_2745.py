'''
    제출 언어: PyPy3
    시간: 112ms
    ord: 문자를 유니코드로 변환 시키는 함수
    chr: 유니코드를 문자로 변환 시키는 함수
''' 
import sys

def convertor(N, B):
    global num_dict

    res = 0
    length = len(N)
    for idx in range(length):
        cur_num = None
        
        if not N[idx].isdecimal():
            cur_num = ord(N[idx]) - 55
        else:
            cur_num = int(N[idx])

        res += pow(B, length - (idx+1)) * cur_num

    return res

if __name__ == "__main__":
    N, B = sys.stdin.readline().strip().split()
    B = int(B)
    
    res = convertor(N, B)
    print(res)
    