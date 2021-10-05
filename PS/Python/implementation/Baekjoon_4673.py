'''
    제출 언어: Python3
    시간: 84ms
'''
def d(num):
    global is_self

    res = num

    for c in str(num):
        res += int(c)
    
    if res < 10001 and is_self[res] == None:
        is_self[res] = False
        d(res)

    pass

if __name__ == "__main__":
    is_self = [None] * 10001

    is_self[1] = True

    d(1)
    print(1)

    for i in range(2, 10001):
        if is_self[i] is None:
            is_self[i] = True
            d(i)
            print(i)
