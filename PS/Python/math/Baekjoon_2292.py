import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())

    answer = 1
    a = 1
    b = 1


    while True:
        a += 6 * (b-1)

        if N <= a:
            answer = b
            break
        
        b += 1
        
    print(answer)
